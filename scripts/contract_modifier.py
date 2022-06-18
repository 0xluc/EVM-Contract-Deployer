import re

# Each key needs to be in the contract
var_defaults = {
    "name": " ",
    "ticker": " ",
    "telegram": " ",
    "website": " ",
    "liquidity-fee": "5",
    "marketing-fee": "5",
    "reflections":"5",
    "numero-de-moedas": "100000000",
    "carteira-marketing": "0x63B1243E3605d8b33a8a6492e213216Dd0dACF99"
}

def debug(inp) :
    #print(inp)
    return inp

# If there is no default value on a var_defaults key, it throws an error
def getvar(name, default) :
    ret = input(f'Value of {name} (default "{default}"): ')
    if not ret :
        if not default : raise Exception("Unset default")
        return default
    return ret

if __name__=="__main__" :
    # loads the contract text on a variable
    contract_gen = ""
    with open("scripts/contractus.sol", 'r') as contract :
        contract_gen = contract.read()

    # search for '<-- -->' in the contract and check if de value is in var_defaults
    var_current = {}
    for match in re.finditer(re.compile(r"<--([a-z0-9\-]+)-->"), contract_gen) :
        var = match.group(1)
        if var not in var_defaults:
            raise Exception("Unchecked variable:", var)
        # if it does find it, then adds the entry made by the user to var_current
        if var not in var_current : var_current[var] = getvar(var, var_defaults[var])


    pattern = debug(r'|'.join(sorted("<--("+re.escape(k)+")-->" for k in var_current)))
    
    contract_gen = re.sub(pattern, lambda m: debug(var_current[next(filter(bool, m.groups()))]), contract_gen)

    with open("contracts/out.sol", "w+") as out_contract :
        out_contract.write(contract_gen)