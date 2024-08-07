# Schema

## USDC ([Link to Box](https://upenn.box.com/s/gft9i4r8q34oc7769o7405w92nskys77))

We've parsed events emitted by [USDC contract](https://etherscan.io/address/0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48) using this [Ethereum Log Parser](https://github.com/niuniu-zhang/Ethereum-Log-Parser)
and uploaded them into [Box](https://upenn.box.com/s/gft9i4r8q34oc7769o7405w92nskys77). In total, we've parsed 14 events:
1. `Approval`
2. `AuthorizationUsed`
3. `Blacklisted`
4. `BlacklisterChanged`
5. `AuthorizationCanceled`
6. `Burn`
7. `MasterMinterChanged`
8. `Mint`
9. `MinterConfigured`
10. `MinterRemoved`
11. `OwnershipTransferred`
12. `PauserChanged`
13. `Transfer`
14. `UnBlacklisted`

Here are the descriptions of schema for each event:

### Approval

The file `usdc_Approval.csv` contains all the "Approval" events emitted by the relevant USDC contract. The dataset includes the following fields:

* `event` - The name of the event (in this case, "Approval").
* `logIndex` - The index of this specific event within the transaction.
* `transactionIndex` - The index position of the transaction within the block.
* `transactionHash` - The hash of the transaction that triggered this event.
* `address` - The address of the contract that generated this event.
* `blockHash` - The hash of the block where this event was recorded.
* `blockNumber` - The number of the block where this event was recorded.
* `owner` - The address of the owner in the approval event.
* `spender` - The address of the spender in the approval event.
* `value` - The value involved in the approval event.
* `block_timestamp` - The timestamp of the block where this event was recorded.

### AuthorizationCanceled

The file `usdc_AuthorizationCanceled.csv` contains all the "AuthorizationCanceled" events emitted by the relevant USDC contract. The dataset includes the following fields:

* `event` - The name of the event (in this case, "AuthorizationCanceled").
* `logIndex` - The index of this specific event within the transaction.
* `transactionIndex` - The index position of the transaction within the block.
* `transactionHash` - The hash of the transaction that triggered this event.
* `address` - The address of the contract that generated this event.
* `blockHash` - The hash of the block where this event was recorded.
* `blockNumber` - The number of the block where this event was recorded.
* `authorizer` - The address of the authorizer in the event.
* `nonce` - The nonce associated with the canceled authorization.
* `block_timestamp` - The timestamp of the block where this event was recorded.

### AuthorizationUsed

The file `usdc_AuthorizationUsed.csv` contains all the "AuthorizationUsed" events emitted by the relevant USDC contract. The dataset includes the following fields:

* `event` - The name of the event (in this case, "AuthorizationUsed").
* `logIndex` - The index of this specific event within the transaction.
* `transactionIndex` - The index position of the transaction within the block.
* `transactionHash` - The hash of the transaction that triggered this event.
* `address` - The address of the contract that generated this event.
* `blockHash` - The hash of the block where this event was recorded.
* `blockNumber` - The number of the block where this event was recorded.
* `authorizer` - The address of the authorizer in the event.
* `nonce` - The nonce used in the authorization.
* `block_timestamp` - The timestamp of the block where this event was recorded.

### Blacklisted

The file `usdc_Blacklisted.csv` contains all the "Blacklisted" events emitted by the relevant USDC contract. The dataset includes the following fields:

* `event` - The name of the event (in this case, "Blacklisted").
* `logIndex` - The index of this specific event within the transaction.
* `transactionIndex` - The index position of the transaction within the block.
* `transactionHash` - The hash of the transaction that triggered this event.
* `address` - The address of the contract that generated this event.
* `blockHash` - The hash of the block where this event was recorded.
* `blockNumber` - The number of the block where this event was recorded.
* `_account` - The address of the account that was blacklisted.
* `block_timestamp` - The timestamp of the block where this event was recorded.

### BlacklisterChanged

The file `usdc_BlacklisterChanged.csv` contains all the "BlacklisterChanged" events emitted by the relevant USDC contract. The dataset includes the following fields:

* `event` - The name of the event (in this case, "BlacklisterChanged").
* `logIndex` - The index of this specific event within the transaction.
* `transactionIndex` - The index position of the transaction within the block.
* `transactionHash` - The hash of the transaction that triggered this event.
* `address` - The address of the contract that generated this event.
* `blockHash` - The hash of the block where this event was recorded.
* `blockNumber` - The number of the block where this event was recorded.
* `newBlacklister` - The address of the new blacklister set in the event.
* `block_timestamp` - The timestamp of the block where this event was recorded.

### Burn

The file `usdc_Burn.csv` contains all the "Burn" events emitted by the relevant USDC contract. The dataset includes the following fields:

* `event` - The name of the event (in this case, "Burn").
* `logIndex` - The index of this specific event within the transaction.
* `transactionIndex` - The index position of the transaction within the block.
* `transactionHash` - The hash of the transaction that triggered this event.
* `address` - The address of the contract that generated this event.
* `blockHash` - The hash of the block where this event was recorded.
* `blockNumber` - The number of the block where this event was recorded.
* `burner` - The address of the burner in the event.
* `amount` - The amount of USDC burned.
* `block_timestamp` - The timestamp of the block where this event was recorded.

### MasterMinterChanged

The file `usdc_MasterMinterChanged.csv` contains all the "MasterMinterChanged" events emitted by the relevant USDC contract. The dataset includes the following fields:

* `event` - The name of the event (in this case, "MasterMinterChanged").
* `logIndex` - The index of this specific event within the transaction.
* `transactionIndex` - The index position of the transaction within the block.
* `transactionHash` - The hash of the transaction that triggered this event.
* `address` - The address of the contract that generated this event.
* `blockHash` - The hash of the block where this event was recorded.
* `blockNumber` - The number of the block where this event was recorded.
* `newMasterMinter` - The address of the new Master Minter.
* `block_timestamp` - The timestamp of the block where this event was recorded.

### Mint

The file `usdc_Mint.csv` contains all the "Mint" events emitted by the relevant USDC contract. The dataset includes the following fields:

* `event` - The name of the event (in this case, "Mint").
* `logIndex` - The index of this specific event within the transaction.
* `transactionIndex` - The index position of the transaction within the block.
* `transactionHash` - The hash of the transaction that triggered this event.
* `address` - The address of the contract that generated this event.
* `blockHash` - The hash of the block where this event was recorded.
* `blockNumber` - The number of the block where this event was recorded.
* `minter` - The address of the minter.
* `to` - The address to which the USDC is minted.
* `amount` - The amount of USDC minted.
* `block_timestamp` - The timestamp of the block where this event was recorded.

### MinterConfigured

The file `usdc_MinterConfigured.csv` contains all the "MinterConfigured" events emitted by the relevant USDC contract. The dataset includes the following fields:

* `event` - The name of the event (in this case, "MinterConfigured").
* `logIndex` - The index of this specific event within the transaction.
* `transactionIndex` - The index position of the transaction within the block.
* `transactionHash` - The hash of the transaction that triggered this event.
* `address` - The address of the contract that generated this event.
* `blockHash` - The hash of the block where this event was recorded.
* `blockNumber` - The number of the block where this event was recorded.
* `minter` - The address of the minter being configured.
* `minterAllowedAmount` - The allowed amount for the minter.
* `block_timestamp` - The timestamp of the block where this event was recorded.

### MinterRemoved

The file `usdc_MinterRemoved.csv` contains all the "MinterRemoved" events emitted by the relevant USDC contract. The dataset includes the following fields:

* `event` - The name of the event (in this case, "MinterRemoved").
* `logIndex` - The index of this specific event within the transaction.
* `transactionIndex` - The index position of the transaction within the block.
* `transactionHash` - The hash of the transaction that triggered this event.
* `address` - The address of the contract that generated this event.
* `blockHash` - The hash of the block where this event was recorded.
* `blockNumber` - The number of the block where this event was recorded.
* `oldMinter` - The address of the minter being removed.
* `block_timestamp` - The timestamp of the block where this event was recorded.

### OwnershipTransferred

The file `usdc_OwnershipTransferred.csv` contains all the "OwnershipTransferred" events emitted by the relevant USDC contract. The dataset includes the following fields:

* `event` - The name of the event (in this case, "OwnershipTransferred").
* `logIndex` - The index of this specific event within the transaction.
* `transactionIndex` - The index position of the transaction within the block.
* `transactionHash` - The hash of the transaction that triggered this event.
* `address` - The address of the contract that generated this event.
* `blockHash` - The hash of the block where this event was recorded.
* `blockNumber` - The number of the block where this event was recorded.
* `previousOwner` - The address of the previous owner.
* `newOwner` - The address of the new owner.
* `block_timestamp` - The timestamp of the block where this event was recorded.

### PauserChanged

The file `usdc_PauserChanged.csv` contains all the "PauserChanged" events emitted by the relevant USDC contract. The dataset includes the following fields:

* `event` - The name of the event (in this case, "PauserChanged").
* `logIndex` - The index of this specific event within the transaction.
* `transactionIndex` - The index position of the transaction within the block.
* `transactionHash` - The hash of the transaction that triggered this event.
* `address` - The address of the contract that generated this event.
* `blockHash` - The hash of the block where this event was recorded.
* `blockNumber` - The number of the block where this event was recorded.
* `newAddress` - The address of the new pauser.
* `block_timestamp` - The timestamp of the block where this event was recorded.

### Transfer

The file `usdc_Transfer.csv` contains all the "Transfer" events emitted by the relevant USDC contract. The dataset includes the following fields:

* `event` - The name of the event (in this case, "Transfer").
* `logIndex` - The index of this specific event within the transaction.
* `transactionIndex` - The index position of the transaction within the block.
* `transactionHash` - The hash of the transaction that triggered this event.
* `address` - The address of the contract that generated this event.
* `blockHash` - The hash of the block where this event was recorded.
* `blockNumber` - The number of the block where this event was recorded.
* `from` - The address of the sender in the transfer event.
* `to` - The address of the receiver in the transfer event.
* `value` - The value of the transfer.
* `block_timestamp` - The timestamp of the block where this event was recorded.

### UnBlacklisted

The file `usdc_UnBlacklisted.csv` contains all the "UnBlacklisted" events emitted by the relevant USDC contract. The dataset includes the following fields:

* `event` - The name of the event (in this case, "UnBlacklisted").
* `logIndex` - The index of this specific event within the transaction.
* `transactionIndex` - The index position of the transaction within the block.
* `transactionHash` - The hash of the transaction that triggered this event.
* `address` - The address of the contract that generated this event.
* `blockHash` - The hash of the block where this event was recorded.
* `blockNumber` - The number of the block where this event was recorded.
* `_account` - The address of the account that was unblacklisted.
* `block_timestamp` - The timestamp of the block where this event was recorded.

## Circle CCTP Smart Contracts for EVM-compatible blockchains ([Link to Box](https://upenn.box.com/s/0yrla120kznl23fkfcf3hqi91n0n5ero))

We have parsed events emitted by the following [CCTP smart contracts](https://developers.circle.com/stablecoins/docs/evm-smart-contracts), each with its specific responsibilities:

### [TokenMessenger Contract](https://etherscan.io/address/0xbd3fa81b58ba92a82136038b25adec7066af3155)

**Responsibilities:**
- Entrypoint for cross-chain USDC transfer.
- Routes messages to burn USDC on a source chain, and mint USDC on a destination chain.

**Events:**

- `DepositForBurn` - Details events related to deposit for burn operations.
- `LocalMinterAdded` - Records the addition of local minters.
- `MintAndWithdraw` - Logs events of minting and withdrawal actions.
- `OwnershipTransferred` - Tracks ownership transfer events.
- `OwnershipTransferStarted` - Indicates the initiation of an ownership transfer.
- `RemoteTokenMessengerAdded` - Logs the addition of remote token messengers.
- `RemoteTokenMessengerRemoved` - Tracks the removal of remote token messengers.
- `RescuerChanged` - Records changes in the rescuer role.


### [MessageTransmitter Contract](https://etherscan.io/address/0x0a992d191deec32afe36203ad87d7d289a738f81)

**Responsibilities:**
- Generic message passing.
- Sends all messages on the source chain, and receives all messages on the destination chain.

**Events:**

- `AttesterEnabled` - Indicates enabling of an attester.
- `AttesterManagerUpdated` - Logs updates to the attester manager.
- `MessageReceived` - Tracks the reception of messages.
- `MessageSent` - Logs the sending of messages.
- `OwnershipTransferred` - Tracks ownership transfer events.
- `OwnershipTransferStarted` - Indicates the initiation of an ownership transfer.
- `PauserChanged` - Logs changes in the pauser role.
- `RescuerChanged` - Records changes in the rescuer role.
- `SignatureThresholdUpdated` - Updates the signature threshold.

### [TokenMinter Contract](https://etherscan.io/address/0xc4922d64a24675e16e1586e3e3aa56c06fabe907)

**Responsibilities:**
- Responsible for minting and burning USDC.
- Contains chain-specific settings used by burners and minters.

**Events:**

- `LocalTokenMessengerAdded` - Indicates the addition of a local token messenger.
- `OwnershipTransferred` - Tracks ownership transfer events.
- `OwnershipTransferStarted` - Indicates the initiation of an ownership transfer.
- `PauserChanged` - Logs changes in the pauser role.
- `SetBurnLimitPerMessage` - Sets the burn limit per message.
- `SetTokenController` - Specifies the setting of a token controller.
- `TokenPairLinked` - Records the linking of token pairs.
- `RescuerChanged` - Records changes in the rescuer role.



