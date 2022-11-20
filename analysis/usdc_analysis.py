import pandas as pd

#event_name,block_number,txhash,log_index,timestamp,_account,newBlacklister,minter,minterAllowedAmount,oldMinter,newMasterMinter,to,amount,burner,contract_address
usdc_configs = pd.read_csv("../data/usdc_configs.csv")

events = list(usdc_configs.event_name.unique())

print( usdc_configs.groupby(['event_name']).size() )

#print( f"Events are: {events}" )

blacklists = usdc_configs.loc[usdc_configs.event_name=='Blacklisted']
unblacklists = usdc_configs.loc[usdc_configs.event_name=='UnBlacklisted']

interesting_blocks = list( blacklists['block_number'].unique() )

print( "=============================" )
print( f"Frozen addresses ({len(blacklists._account)})\n" )

for a in blacklists._account:
	if a not in unblacklists._account:
		print( a )
	else:
		print( f"{a} (Subsequently un-frozen)" )

if 'msg.sender' in blacklists.columns:
	print( blacklists.groupby(['msg.sender']).size() )	
else:
	print( "The 'Blacklisted' event does *not* record the blacklister" )
	print( "Run the script ../addSender.py and try again" )

print( "=============================" )
print( "Minting stats\n" )

#blacklisted_addresses = blacklists['_account']
unblacklisted_addresses = list(unblacklists['_account'])

supply = usdc_configs.loc[usdc_configs.event_name.isin(['Mint','Burn'])].copy()
supply.loc[supply.event_name == 'Burn','amount'] *= -1
supply = supply[['timestamp','amount']]
supply['amount']
supply.sort_values(by=['timestamp'],inplace=True)
supply['amount'] = supply['amount'].cumsum()
supply = supply.loc[supply['amount'].ne(supply['amount'].shift())]
supply['timestamp'] = supply['timestamp'].apply(lambda x: x[0:10])

print( f"Max mint = {usdc_configs.loc[usdc_configs.event_name=='Mint']['amount'].max()/10**6}" )
print( f"Min mint = {usdc_configs.loc[usdc_configs.event_name=='Mint']['amount'].min()/10**6}" )

print( f"Max burn = {usdc_configs.loc[usdc_configs.event_name=='Burn']['amount'].max()/10**6}" )
print( f"Min burn = {usdc_configs.loc[usdc_configs.event_name=='Burn']['amount'].min()/10**6}" )

num_minters = len(usdc_configs.loc[usdc_configs.event_name=='Mint']['minter'].unique())
print( f"{num_minters} distinct minters" )

print( "Cumulative number of USDC minted by minter address" )
mintings = usdc_configs.loc[usdc_configs.event_name=='Mint'].groupby(['minter'])['amount'].sum()/10**6
mintings.sort_values(ascending=False,inplace=True)

print( mintings )

print( "Cumulative number of distinct mint events by minter address" )
mintings = usdc_configs.loc[usdc_configs.event_name=='Mint'].groupby(['minter']).size()
mintings.sort_values(ascending=False,inplace=True)
print( mintings )

print( "Cumulative number of USDC minted to address" )
mintings = usdc_configs.loc[usdc_configs.event_name=='Mint'].groupby(['to'])['amount'].sum()/10**6
mintings.sort_values(ascending=False,inplace=True)

print( mintings )

print( "Cumulative number of distinct mint events to address" )
mintings = usdc_configs.loc[usdc_configs.event_name=='Mint'].groupby(['to']).size()
mintings.sort_values(ascending=False,inplace=True)
print( mintings )

#supply.to_csv('usdc_supply.csv',index=False)

#print( interesting_blocks )
