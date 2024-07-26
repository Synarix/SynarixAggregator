from synarixaggregator import SynarixAggregatorModul

# The `SynarixAggregatorModul`(SAM) is a class that provides submoduls and functions to interact with ERC20 Smart Contracts and AMM (DEXs) from version 2 to 3.
SAM = SynarixAggregatorModul(
 settings_file_path="./Settings.json", # set filename and path to config file if you want
 saveSettings=False # if you want to save settings to Settings.json file
)

BUSD = SAM.w3.to_checksum_address("0xe9e7cea3dedca5984780bafc599bd69add087d56")
#Hardhat Node Account#0
dummy_private_key = "0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80" #never use this in public networks!
SAM.loadWalletFromPrivKey(dummy_private_key)
SAM.changeRPC("http://127.0.0.1:8545/")

print(
f"""
Loaded Address is: {SAM.IERC20.user_address}
BNB BALANCE: {SAM.w3U.custom_round(SAM.IAC.getBNBBalance())}
"""
)

#Swap 0.1 BNB to BUSD, use SwapETHtoToken Method
#First we need to change to the token we want to buy or sell
SAM.changeToken(BUSD) 
status, txHash, gas_infos =SAM.IAC.SwapETHtoToken(
 inputAmount=100, # Input amount in float e.g 0.01,1, 3, 0.0123
 trys=1 #If you trade on high demand, sometimes transactions fail, set trys
 )
print(status, txHash, gas_infos) 
if status:
 print("Transaction cost:", gas_infos[1],"BNB")

#get token Balance after swap
token_balance = SAM.IERC20.get_token_balance()
print(SAM.IERC20.get_token_Name(),"Balance:", SAM.IERC20.get_token_balance())

#Swap BUSD balance back to ETH
status, txHash, gas_infos = SAM.IAC.SwapTokentoETH(
   token_balance
 )
if not status:
 #Token is not approved!! 
 print(gas_infos)


#Lets approve token balance and swap again
status, txHash, gas_infos = SAM.IERC20.approveAggregator(token_balance) # if no amount set approve max uint256 -1
print("Transaction cost:", gas_infos[1],"BNB")
print()

#Swap BUSD balance back to ETH
status, txHash, gas_infos = SAM.IAC.SwapTokentoETH(
   token_balance
 )
print(status, txHash, gas_infos )
print("Transaction cost:", gas_infos[1],"BNB")
print()


print(
f"""
BNB BALANCE: {SAM.w3U.custom_round(SAM.IAC.getBNBBalance())}
"""
)
