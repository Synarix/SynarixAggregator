import json
import logging
from typing import Dict
from web3 import Web3

class CoreSettings:
    
    DEFAULT_SETTINGS = {
        "metamask_address": "", # User address, only need for transactions
        "metamask_private_key": "", # Private key, save only to file if you know what you doing, only need for swap transactions, approve, etc
        "RPC": "https://bsc-dataseed1.binance.org/", # RPC to connect web3 make sure chain is supported
        "GWEI_OFFSET": 0, #Estimate gas cost and add offset
        "MaxTXFeeBNB": 0.001, #save you for massive Gas cost 
        "Slippage": 3, # Max Slippage you can accept
        "timeout": 60 # Timeout for waiting web3 requests
    }

    def __init__(self, settings_file_path: str = "./Settings.json", createSettings: bool = False):
        self.createSettings = createSettings
        self.settings_file_path = settings_file_path
        self.settings = self.DEFAULT_SETTINGS.copy()
        self.load_settings()

    def reinit_settings(self):
        self.settings = self.DEFAULT_SETTINGS.copy()
        self.load_settings()

    def load_settings(self):
        try:
            with open(self.settings_file_path, "r") as f:
                user_settings = json.load(f)
            self.settings.update(user_settings)
            self.check_settings()
        except Exception as e:
            if self.createSettings:
                logging.warning("Settings file not found, creating with default settings.")
                self.save_settings_to_file()

    def save_settings_to_file(self):
        try:
            with open(self.settings_file_path, "w") as f:
                json.dump(self.settings, f, indent=4)
            logging.info(f"Settings saved to {self.settings_file_path}")
        except IOError as e:
            logging.error(f"Failed to save settings: {e}")

    def check_settings(self):
        if self.settings.get("metamask_address") and not Web3.is_address(self.settings["metamask_address"]):
            logging.error("Invalid metamask_address in settings!")
            raise ValueError("Invalid metamask_address in settings!")
        if self.settings.get("metamask_private_key") and len(self.settings["metamask_private_key"]) not in [64, 66]:
            logging.error("Invalid metamask_private_key in settings!")
            raise ValueError("Invalid metamask_private_key in settings!")
        
    def change_settings(self, key, newValue):
        self.settings[key] = newValue

    def update_settings(self, new_settings: Dict[str, any]):
        updatable_keys = {k: v for k, v in new_settings.items() if k not in ["RPC", "timeout", "GWEI_OFFSET"]}
        self.settings.update(updatable_keys)
        self.check_settings()
        self.save_settings()