from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_abi import abi
from .core_abis import IERC20_ABI  # Adjust the import path as necessary

class IERC20:
    def __init__(self, settings, w3, token, w3U):
        self.settings, self.user_address, self.priv_key, self.w3, self.token, self.w3U = settings, settings.settings["metamask_address"], settings.settings["metamask_private_key"], w3, token, w3U
        self.token_Instance = self.init_token_instance()
        
    def init_token_instance(self):
        token_Instance = self.w3.eth.contract(
            address=Web3.to_checksum_address(self.token), abi=IERC20_ABI)
        return token_Instance
    
    def get_token_balance(self, address):
        return self.w3U.from_wei(self.get_token_balance_(address) , self.get_token_decimals())
    
    def get_token_allowance(self, spender):
        return self.w3U.from_wei(self.get_token_allowance_(spender) , self.get_token_decimals())
    
    def get_token_address(self):
        return Web3.to_checksum_address(self.token_Instance.address)

    def get_token_decimals(self):
        return self.token_Instance.functions.decimals().call()

    def get_token_Name(self):
        return self.token_Instance.functions.name().call()

    def get_token_Symbol(self):
        return self.token_Instance.functions.symbol().call()
    
    def get_token_balance_(self, address):
        return self.token_Instance.functions.balanceOf(Web3.to_checksum_address(address)).call()
    
    def get_token_allowance(self, spender):
        return self.token_Instance.functions.allowance(self.user_address, spender).call()
    
    def is_approved(self, spender, amountIn):
        allowance = self.get_token_allowance(spender)
        if int(allowance) >= int(amountIn):
            return True
        else:
            return False
        
    def approve(self, spender, amountIn):
        if self.is_approved(spender, amountIn) == False:
            txn = self.token_Instance.functions.approve(
                Web3.to_checksum_address(spender),
                2**256 - 1
            ).build_transaction(
                {'from': self.user_address,
                 'gasPrice': self.w3.eth.gas_price + Web3.to_wei(self.settings.settings["GWEI_OFFSET"], "gwei"),
                 'nonce': self.w3.eth.get_transaction_count(self.user_address),
                 'value': 0}
            )
            gas = self.w3U.estimateGas(txn)
            txn.update({'gas': int(gas[0])})
            signed_txn = self.w3.eth.account.sign_transaction(
                txn,
                self.priv_key
            )
            txn = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            txn_receipt = self.w3.eth.wait_for_transaction_receipt(
                txn, timeout=self.settings.settings["timeout"])
            if txn_receipt['status'] == 1:
                return True, txn.hex(), gas[1]
            else:
                return False, txn.hex(), gas[1]
        else:
            return True, "Already Approved", ""
            
