from synarixaggregator import SynarixAggregatorModul
SAM = SynarixAggregatorModul()
#Hi Sam!

SAM.changeToken(
  "0xba2ae424d960c26247dd6c32edc70b295c744c43" #Binance Pegged Dogecoin
)

symbol = SAM.IERC20.get_token_Symbol() # get symbol
usdPrice = SAM.IAC.getUSDPrice() # get usd price
liquidity = SAM.IAC.getLiquidityUSD() # get Liquidity in usd


print(
f"""
TokenSymbol: {symbol}
Token Price: {usdPrice} $
Token Liquidity: {liquidity} $
"""
)

# ok, we can print floats better
clean_price = SAM.w3U.custom_round(usdPrice)
clean_liquidity = SAM.w3U.custom_round(liquidity)

print(
f"""
TokenSymbol: {symbol}
Token Price: {clean_price} $
Token Liquidity: {clean_liquidity} $
"""
)

#Gater some information about the token, its simulate buy and sell transaction to calculate Token Fees/loss
#Check token infos, Tax and simulate a Buy and Sell transaction to check for honeypot
buy_tax, sell_tax, ishoneypot = SAM.IAC.getTokenInfos() 
print(
f"""
Is Token Scam/Honeypot? : {ishoneypot}
Tax On Buy Transaction:  {buy_tax}%
Tax On Sell Transaction:  {sell_tax}%
""")
