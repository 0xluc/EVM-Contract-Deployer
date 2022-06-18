## Pre-requirements
You need to install brownie and start it in the folder where your deployer will be
```bash
pip install eth-brownie 
brownie init
```
## Installation
- Copy the files from the scripts folder to your scripts folder
- Copy the deploy file to the main folder
- Change the file contractus.sol to the contract you will be using
- Insert the variables in the contract or remove the ones you will not use from var_defaults in the contract_modifier.py file
- Run the deploy file, remember to do ```chmod +x``` before