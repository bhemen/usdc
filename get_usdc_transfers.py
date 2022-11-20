"""
Scan the chain for events relating to configuration changes in the USDC token contract
Record:
Transfer
"""

api_url = 'http://127.0.0.1:8545'
start_block = 6082465 
contract_address = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48" 
outfile = "data/usdc_transfers.csv"
scanned_events = ["Transfer"]

from tools.get_contract_events import getContractEvents

getContractEvents(api_url,start_block,contract_address,outfile,scanned_events)

