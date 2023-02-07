from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/743ef74b4cc149f298131d204ba83999'))
account = w3.eth.account.create()
privateKey = account.key.hex()
address = account.address

print(f"Your address: {address}\nYour key: {privateKey}")