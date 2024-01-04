from web3 import Web3
from tqdm.auto import tqdm
import pandas as pd
from utils import get_cached_abi
from datetime import datetime
import sys
import csv

def restoreState(outfile):
	try:
		df = pd.read_csv(outfile)
	except Exception as e:
		return [], 0

	if len(df) == 0:
		return [], 0

	start_block = int(df.blockNumber.max())

	df = df[df.blockNumber != start_block] #It's possible that scraping failed in the middle of the last block, so we delete those rows
	df.to_csv(outfile,index=False)

	print( f"Restoring from {outfile}" )
	print( f"Starting at {start_block}" )
	return df.columns, start_block

def getContractEvents( contract_address, target_events, outfile, api_url="127.0.0.1:8545",start_block=1,end_block=None ):
	"""
		contract_address - the address of the contract to scrape
		target_events - list of names of events you want to scrape (if target_events = 'all' then, we scrape all events from the contract)
		outfile - where to write the .csv of events
		api_url - the url of the Ethereum node
		start_block - the block number to start scanning (you should often set this to be the deploy block of the contract)
		end_block - scan until this block.  If end_block == None, then scan until the end of the chain
	"""
	w3 = Web3(Web3.HTTPProvider(api_url))

	error_file = outfile.split(".")[0] + "_errors.csv"

	contract_address = Web3.to_checksum_address(contract_address)
	latest_block = w3.eth.get_block_number() #Last block your node knows about

	if end_block == None: #If no end_block was provided to the function, scan to the end of the chain
		end_block = latest_block
	
	batch_size = base_batch_size = 100 #How many blocks to scan at once

	max_retries = 5 #Maximum number of times you'll retry a query if the node returns an error
	num_retries = 0
	abi = get_cached_abi(contract_address) #Calls the utils library to get the ABI from the local cache.  If the ABI is not in the local cache it queries etherscan

	contract = w3.eth.contract(address=contract_address,abi=abi) #Make a contract object

	#Create a mapping from event "signatures" to event names
	#The signature of an event is the keccak hash of the name of the event (and its arguments)
	#We can calculate the signatures from the ABI
	#The "signature" for the Transfer event is keccak("Transfer(address,address,uint256)")
	#Which is 0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef
	full_event_signatures = {}
	event_signatures = {}
	for evt in [obj for obj in abi if obj['type'] == 'event']:
		name = evt['name']
		types = [inpt['type'] for inpt in evt['inputs']]
		full = '{}({})'.format(name,','.join(types))
		sig = Web3.keccak(text=full).hex() #Signature is keccak applied to EventName(event_inputs)
		full_event_signatures[sig] = full #This map has the "full" name (with inputs included).  For example full_event_signatures["0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"] = "Transfer(address,address,uint256)"
		event_signatures[sig] = name #This map has only the name.  For example event_signatures["0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"] = "Transfer"

	if target_events == 'all' or target_events == []:
		target_event_signatures = event_signatures
	else:
		target_event_signatures = { k:v for k,v in event_signatures.items() if v in target_events }
		if len(target_event_signatures.values()) < len(target_events):
			print( f"Error: you specified an event that doesn't exist in the contract" )
			print( f"events = {target_event_signatures.values()}" )
			print( f"target_events = {target_events}" )
			print( event_signatures )
			sys.exit(1)

	#We will have a column in the csv for every input to every Event we are searching for
	#So this gets a list of all the Event inputs
	colnames = set()
	for evt in [obj for obj in abi if obj['type'] == 'event' and obj['name'] in target_event_signatures.values()]:
		colnames = colnames.union( [inpt['name'] for inpt in evt['inputs']] )

	#These are extra columns we record for every event
	extra_cols = ['event','address','blockHash','blockNumber','timestamp','transactionHash','msg.sender','data']
	colnames = sorted( list( colnames.union(extra_cols) ) )	#Sort the columns to make sure they all line when you restore from a partial scraping
	print( f'colnames = {colnames}' )

	old_cols, last_scanned_block = restoreState(outfile)

	if last_scanned_block > 0: #We have a state to restore
		if len(old_cols) > 0: #Check that the old state is consistent with the new state (Check that the old set of columns is the same as the new set of columns)
			if set(old_cols) != set(colnames):
				print( f"Error: restored state has a different set of columns" )
				if len( set(colnames).difference(old_cols) ) > 0:
					print( f"Error: events have columns not in existing data set {list(set(colnames).difference(old_cols))}" )
				if len( set(old_cols).difference(colnames) ) > 0:
					print( f"Error: old_columns not in existing data set {list(set(old_cols).difference(colnames))}" )
				sys.exit(1) #If the old set of columns doesn't match the new set, then we abort

		start_block = max( last_scanned_block, start_block ) #Pick up where we left off
	else: #Starting from scratch, so we write the column names
		with open( outfile, 'w' ) as f:
			w = csv.DictWriter( f, fieldnames=colnames )
			w.writeheader()

	print( f"Scanning for events {list(target_event_signatures.values())}" )
	print( f"Writing data to {outfile}" )

	batch_start_block = start_block
	formatted_time = ""
	events_count = 0

	#Loop over all blocks in the chain
	#We use a while loop instead of a for loop so that we can loop over variable sized batches of blocks
	with tqdm(total=end_block-start_block) as bar:
		while True:
			batch_end_block = min( batch_start_block + batch_size, latest_block )
			if batch_start_block >= min( latest_block, end_block ):
				break
			try:
				events = [list(target_event_signatures.keys())] #Note the double-list: https://ethereum.stackexchange.com/questions/90526/web3-py-topics
				#lgs = w3.eth.get_logs( { 'fromBlock': start_block, 'toBlock': end_block, 'address': contract_address, 'topics': events } )
				lgs = w3.eth.get_logs( { 'fromBlock': batch_start_block, 'toBlock': batch_end_block, 'address': contract_address } ) #This is where we call the chain
			except Exception as e:
				print( "Error" )
				print( e )
				batch_size = max( batch_size // 2, 1 ) #If we get an error, we halve the batch size
				num_retries += 1
				if num_retries == max_retries: 
					num_retries = 0
					with open(error_file,"a") as f:
						f.write(f"{start_block} : {e}\n" )
					start_block += 1
				continue

			if len(lgs) > 0:
				new_rows = processLogs(w3,contract,target_event_signatures,lgs)	#Returns a list of dictionaries
				if len(new_rows) > 0:
					with open( outfile, 'a' ) as f:
						w = csv.DictWriter( f, fieldnames=colnames )
						w.writerows( new_rows )
					
					if 'timestamp' in new_rows[-1].keys():
						formatted_time = datetime.fromtimestamp(new_rows[-1]['timestamp']).strftime("%Y-%m-%d")
					events_count = len(new_rows)

			bar.set_description(f"Current block: {batch_start_block} ({formatted_time}) blocks in a scan batch: {batch_size}, events processed in a batch {events_count}")
			bar.update(batch_size)

			batch_start_block = batch_end_block + 1
			batch_size = min( batch_size*2, base_batch_size )
			num_retries = 0

def processLogs(w3,contract,event_signatures,lgs):
	"""
		w3 - w3 instance (needed to get the block timestamp, and msg.sender which are not included in the logs)
		contract - contract object
		event_signatures - dictionary of signature -> name mappings for the events we care about
		lgs - list of contract logs returned by get_logs

		Returns a list of dicts
	"""
	rows = []
	for lg in lgs:
		row = {'address': lg.address, 'blockHash': lg.blockHash.hex(), 'blockNumber': lg.blockNumber, 'transactionHash': lg.transactionHash.hex(), 'data': lg.data }
		try:
			timestamp = w3.eth.get_block(lg.blockNumber).timestamp
			row['timestamp'] = timestamp
		except Exception as e:
			print( f"Failed to get timestamp" )
			print( e )
			pass
			

		if lg.topics[0].hex() in event_signatures.keys(): #Only grab the events in our list
			event = event_signatures[lg.topics[0].hex()] #Look up event name in the dictionary we made
			event_obj = getattr( contract.events, event ) #Get the function needed to process the log from the contract object
			logs = event_obj().process_log(lg)
			if 'args' in logs.keys():
				row.update( logs['args'] )
		else:
			continue
			#event = lg.topics[0].hex()
			#print( f"Skipping {event}" )

		row['event'] = event

		try:
			tx = w3.eth.get_transaction(lg.transactionHash)
			row['msg.sender'] = tx['from'] #What was the address that called the method that generated this event
		except Exception as e:
			row['msg.sender'] = None
	
		rows.append(row)

	return rows
				

if __name__ == '__main__':
	deploy_block = start_block = 10926829
	contract_address = "0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9" #AAVE token
	contract_address = "0x1f9840a85d5af5bf1d1762f925bdaddc4201f984" #UNI token

	contract_address = Web3.to_checksum_address(contract_address)
	target_events = ['Transfer']

	outfile = "data/uni_token_logs.csv"

	getContractEvents( contract_address, target_events, outfile, deploy_block ,end_block=None )
