"""
Scan the chain for events relating to configuration changes in the USDC token contract
Record:
Mint
Burn
MinterConfigured
MinterRemoved
MasterMinterChanged
Blacklisted
UnBlacklisted
BlacklisterChanged
"""

api_url = 'http://127.0.0.1:8545'
start_block = 6082465 
tokenMessenger = "0xbd3fa81b58ba92a82136038b25adec7066af3155"
messageTransmitter = "0x0a992d191deec32afe36203ad87d7d289a738f81"
messengerFile = "data/CCTP_Messenger.csv"
transmitterFile = "data/CCTP_Transmitter.csv"
scanned_events = 'all'

from tools.get_contract_events import getContractEvents
contract_address = tokenMessenger
outfile = messengerFile
getContractEvents(api_url,start_block,contract_address,outfile,scanned_events)

contract_address = messageTransmitter
outfile = transmitterFile
getContractEvents(api_url,start_block,contract_address,outfile,scanned_events)

