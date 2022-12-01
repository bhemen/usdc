# Python scripts for analyzing USDC on Ethereum

## USDC

USDC is a fiat-backed stablecoin issued by Circle.  You can read about the off-chain reserves backing USDC at Circle's [transparency](https://www.circle.com/en/usdc#transparency) page.
Circle currently issues USDC on [9 blockchains](https://www.circle.com/en/multichain-usdc), but this repository focuses on the contracts that control USDC on Ethereum.
On Ethereum, USDC is implemented as an ERC-20 contract, but it has significant additional functionality beyond the minimum specified by the [ERC-20 standard](https://ethereum.org/en/developers/docs/standards/tokens/erc-20/).

This repository is provided to aid in analysis of the on-chain use of USDC.  If you are considering *using* USDC, please read the [terms of service](https://www.circle.com/en/legal/usdc-terms).

## Contract overview

The USDC contract is deployed at [0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48](https://etherscan.io/address/0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48).

The source code for is available at [Centre's github repository](https://github.com/centrehq/centre-tokens).

Following [OpenZeppelin standards](https://docs.openzeppelin.com/contracts/2.x/api/ownership#Ownable), the USDC contract is "ownable", 
and the owner is [0xFcb19e6a322b27c06842A71e8c725399f049AE3a](https://etherscan.io/address/0xFcb19e6a322b27c06842A71e8c725399f049AE3a).

The contract is also "[Pausable](https://docs.openzeppelin.com/contracts/4.x/api/security#Pausable)", meaning that the owner can pause the contract at will.  In the context of 
USDC, pausing the contract prevents all [transfers](https://github.com/centrehq/centre-tokens/blob/master/contracts/v1/FiatTokenV1.sol#L275) (including mints and burns).

The contract is "[Blacklistable](https://github.com/centrehq/centre-tokens/blob/master/contracts/v1/Blacklistable.sol)", meaning that special accounts ("Blacklisters") can selectively 
freeze the funds of target users.  Basically, the contract will not process transfers [to](https://github.com/centrehq/centre-tokens/blob/master/contracts/v1/FiatTokenV1.sol#L276) or from "Blacklisted" addresses.
Since mints and burns are special types of transfers, you cannot mint funds to or burn funds from a "blacklisted" address.
Unlike the "Ownable" and "Pausable" which were standardized by OpenZeppelin and used by a wide variety of contracts, the Blacklistable property was developed by Centre and the code seems to be specific to the USDC 
contract.  Other fiat-backed stablecoins (e.g. USDT, USDP, BUSD) implement a similar functionality, but with different terminology and code.

## Tools

[get_usdc_configs.py](get_usdc_configs.py) Will scrape all "configuration" events from the USDC contract.  Specifically, it scans the Ethereum blockchain for the following events, 
and records them to [data/usdc_configs.csv](data/usdc_configs.csv).

* [Mint](https://github.com/centrehq/centre-tokens/blob/master/contracts/v1/FiatTokenV1.sol#L53)
* [Burn](https://github.com/centrehq/centre-tokens/blob/master/contracts/v1/FiatTokenV1.sol#L54)
* [MinterConfigured](https://github.com/centrehq/centre-tokens/blob/master/contracts/v1/FiatTokenV1.sol#L55)
* [MinterRemoved](https://github.com/centrehq/centre-tokens/blob/master/contracts/v1/FiatTokenV1.sol#L56)
* [MasterMinterChanged](https://github.com/centrehq/centre-tokens/blob/master/contracts/v1/FiatTokenV1.sol#L57)0
* [Blacklisted](https://github.com/centrehq/centre-tokens/blob/master/contracts/v1/Blacklistable.sol#L37)
* [UnBlacklisted](https://github.com/centrehq/centre-tokens/blob/master/contracts/v1/Blacklistable.sol#L38)
* [BlacklisterChanged](https://github.com/centrehq/centre-tokens/blob/master/contracts/v1/Blacklistable.sol#L39)

The file [analysis/usdc_analysis.py](analysis/usdc_analysis.py) does some basic analytics, e.g. counting the number of mints and burns by minter address.

## Who's in charge?

USDC is a proxy contract, meaning that the contract functionality can be changed at any time by the "owner"

USDC is also pausable, meaning that it can be paused at any time by the "owner" [0xFcb19e6a322b27c06842A71e8c725399f049AE3a](https://etherscan.io/address/0xFcb19e6a322b27c06842A71e8c725399f049AE3a).  When the contract is paused, no USDC can be minted, burned, frozen or transferred until the owner unpauses the contract.

### Minting

As of block [15590765](https://etherscan.io/block/15590765), only three addresses have minted USDC. 
1. [0x5B6122C109B78C6755486966148C1D70a50A47D7](https://etherscan.io/address/0x5B6122C109B78C6755486966148C1D70a50A47D7)
2. [0x19a932fC5A8320939c3575302a8705147a7f27D8](https://etherscan.io/address/0x19a932fC5A8320939c3575302a8705147a7f27D8)
3. [0x24BDd8771b08C2EA6FE0e898126e65BD49021BE3](https://etherscan.io/address/0x24BDd8771b08C2EA6FE0e898126e65BD49021BE3)

The vast majority has been minted by address 1 (0x5B...).  Address 2 (0x19...) has minted less than 10,000 USDC, and address 3 (0x24..) seems to have been a test address, 
it only minted 200 USDC, and has been inactive since April 10th 2020.

All three addresses are Externally Owned Accounts (EOAs)

USDC has been minted **to** 6 different addresses

1. [0x55FE002aefF02F77364de339a1292923A15844B8](https://etherscan.io/address/0x55FE002aefF02F77364de339a1292923A15844B8)
2. [0xfFADDD32C3670E429884482aFDF9dFB8aff6Ca43](https://etherscan.io/address/0xfFADDD32C3670E429884482aFDF9dFB8aff6Ca43)
3. [0x895F07957B863f4AB6086035a6990d8366Bc3266](https://etherscan.io/address/0x895F07957B863f4AB6086035a6990d8366Bc3266)
4. [0x413a5a3d9451Ac6cAACB759C3514943500156099](https://etherscan.io/address/0x413a5a3d9451Ac6cAACB759C3514943500156099)
5. [0x28C5B0445d0728bc25f143f8EbA5C5539fAe151A](https://etherscan.io/address/0x28C5B0445d0728bc25f143f8EbA5C5539fAe151A)
6. [0x87976bDcBe7ec19a1fbD45dc39ce55C00C4790A1](https://etherscan.io/address/0x87976bDcBe7ec19a1fbD45dc39ce55C00C4790A1)

with the vast majority minted to Address 1 (0x55...).

### Blacklisting

Circle has a brief description of its ["blacklisting" policy available on its website](https://www.centre.io/hubfs/PDF/Centre_Blacklisting_Policy_20200512.pdf).

Blacklisting is controlled by [0x5db0115f3b72d19cea34dd697cf412ff86dc7e1b](https://etherscan.io/address/0x5db0115f3b72d19cea34dd697cf412ff86dc7e1b), which is an EOA.  
This is the only account to have ever called the "[blacklist](https://github.com/centrehq/centre-tokens/blob/master/contracts/v1/Blacklistable.sol#L76)" function.

To date, [150 accounts have been frozen](https://bloxy.info/txs/events_sc/0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48?signature_id=257159)


