from .W3Utils import W3Utils
from .core_settings import CoreSettings
from .core_chains import chains
from .IERC20 import IERC20
from .SynarixAC_F import InterfaceAggregatorContract  
from web3 import Web3
from web3.middleware import geth_poa_middleware

class SynarixAggregatorModul:
    def __init__(self, token:str=None):
        self.settings = CoreSettings()
        self.w3 = self.connect()
        self.w3U = W3Utils(self.settings, self.w3)
        if Web3.is_address(token):
            self.token = Web3.to_checksum_address(token)
            pass
        else:
            print("No Token Addresss Provided fallback to Synarix Governance Token")
            self.token = chains(self.w3.eth.chain_id).RIX
        self.IERC20 = IERC20(self.settings, self.w3, Web3.to_checksum_address(self.token), self.w3U)
        self.IAC = InterfaceAggregatorContract(self.settings, self.w3, self.IERC20, self.w3U)

    def reloadSettings(self):
        self.settings = CoreSettings()
        self.w3 = self.connect()
        self.w3U = W3Utils(self.settings, self.w3)
        self.IERC20 = IERC20(self.settings, self.w3, self.token, self.w3U)
        self.IAC = InterfaceAggregatorContract(self.settings, self.w3, self.IERC20, self.w3U)

    def connect(self):
        keys = self.settings.settings
        if keys["RPC"][:2].lower() == "ws":
            w3 = Web3(Web3.WebsocketProvider(keys["RPC"],request_kwargs={'timeout': int(keys["timeout"])}))
            w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        else:
            w3 = Web3(Web3.HTTPProvider(keys["RPC"], request_kwargs={'timeout': int(keys["timeout"])}))
            w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        return w3
    
    def changeSettings(self, key, newValue):
        self.settings.change_settings(key, newValue)
        self.reloadSettings()
        
    def getSettings(self):
        return self.settings.settings
        
    def changeToken(self, token:str):
       self.IERC20 = IERC20(
            self.settings,
            self.w3,
            Web3.to_checksum_address(token),
            self.w3U
        )
       self.IAC = InterfaceAggregatorContract(self.settings, self.w3, self.IERC20, self.w3U)
       
    






