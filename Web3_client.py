# pyweb3 - A Web3 RPC client for Ethereum compatible wallets in Python

# https://github.com/bitlogik/pyWeb3
# https://pypi.org/project/pyweb3/

#  Installation and requirements: 
# Works with Python >= 3.6.

# Installation of this library
python3 -m pip install pyweb3

# From sources, download and run in this directory :
python3 -m pip install .

"""
Use:
Instanciate with pyweb3.Web3Client, then use methods of this object to send RPC queries.
"""

# Basic example :
from pyweb3 import Web3Client

# Get Token0 address of the ETH/USDT SushiSwap AMM pair on Polygon
amm_pair_contract = "0xc2755915a85c6f6c1c0f3a86ac8c058f11caa9c9"
token0Call = "0dfe1681"  # Keccak256( "token0()" )

rpc_api = Web3Client("https://matic-mainnet.chainstacklabs.com")

# Get token0 address of the pair : WETH
res_hex = rpc_api.call(amm_pair_contract, token0Call)
print(f"Token 0 Address : 0x{res_hex[-40:]}")

