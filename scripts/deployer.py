import os
from brownie import *

def main():
    # Use the enviroment key $KEY as seed phrase
    a.add(os.environ['KEY'])
    # deploys a contract that necessarily needs a working router address
    Contractus.deploy('0x9Ac64Cc6e4415144C455BD8E4837Fea55603e5c3', {'gas_limit':10000000,'from':a[0]})

    # normally it would be done like this> Contractus.deploy({'gas_limit':10000000,'from':a[0]})