from web3 import Web3
from .wallet import *

def sendTransaction(message):
    w3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/743ef74b4cc149f298131d204ba83999'))
    nonce = w3.eth.get_transaction_count(address)
    gasPrice = w3.eth.gas_price
    value = w3.to_wei(0, 'ether')
    signedTx = w3.eth.account.sign_transaction(
        dict(
            nonce = nonce,
            gasPrice = gasPrice,
            gas = 23000,
            to = '0x0000000000000000000000000000000000000000',
            value = value,
            data = message.encode('utf8'),
            chainId = 5
        ), 
        privateKey)

    tx = w3.eth.send_raw_transaction(signedTx.rawTransaction)
    txId = w3.to_hex(tx)
    return txId
