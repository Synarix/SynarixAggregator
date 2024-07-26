from synarixaggregator import SynarixAggregatorModul

# The `SynarixAggregatorModul`(SAM) is a class that provides submoduls and functions to interact with ERC20 Smart Contracts and AMM (DEXs) from version 2 to 3.
SAM = SynarixAggregatorModul(
 settings_file_path="./Settings.json", # set filename and path to config file if you want
 saveSettings=False # if you want to save settings to Settings.json file
)

print("Default Settings Dict:"),SAM.printSettings()

settings = SAM.getSettings()
#print(settings)

#Hardhat Node Account#0
dummy_address = "0xf39fd6e51aad88f6f4ce6ab8827279cfffb92266" #never use this in public networks!
dummy_private_key = "0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80" #never use this in public networks!

#Manual edit Settings wallet
SAM.editSettings(
 key="address",
 newValue=dummy_address,
 skipReload = True # Skip reload of submodules, save time
)
SAM.editSettings(key="private_key", newValue=dummy_private_key, skipReload = True)
SAM.reload() 

# simple import from private key
SAM.loadWalletFromPrivKey(dummy_private_key)
print("Wallet from Priv key imported, new settings:"),SAM.printSettings()

SAM.loadWalletFromMnomic(
   "witness explain monitor check grid depend music purchase ready title bar federal" # DONT USE in PUBLIC networks!
)
print("Wallet from Mnomic seeds imported, new settings:"), SAM.printSettings()

#Lets change the rpc to a faster one like ws or wss
SAM.editSettings(
    key="RPC",
    newValue="wss://bsc-rpc.publicnode.com	", # Hardhat and BSC is currently supported
)

settings = SAM.getSettings()
print(settings["RPC"])


#Connect to Localhost Hardhat Node for testing (https://hardhat.org/hardhat-runner/docs/getting-started)
#Hardhat Node BSC fork Example (https://github.com/Synarix/PancakeSwap_Sniper_Bot_V3andV2/tree/main/hardhat)
#SAM.editSettings(
#    key="RPC",
#    newValue="http://127.0.0.1/8545", # Hardhat and BSC is currently supported
#)
