from synarixaggregator import SynarixAggregatorModul

# The `SynarixAggregatorModul`(SAM) is a class that provides submoduls and functions to interact with ERC20 Smart Contracts and AMM (DEXs) from version 2 to 3.
SAM = SynarixAggregatorModul()
#SAM have kids that priovide good work to him.
#Here is IERC20, sams kid to do work with Token Contract Functions, you can call him like so 
#SAM.IERC20
#Lets give IERC20 a Job: Print token name
print(
  SAM.IERC20.get_token_Name() # Token Name
)
#and now here is IAC he do all the work for Automatet marketmakers in the world of Dex
#IAC give us the price from current initalized token
print(SAM.IAC.getUSDPrice())
#SAM change the Token!
SAM.changeToken(
  "0xba2ae424d960c26247dd6c32edc70b295c744c43"
)
#What token it is?? IERC20!!
SAM.IERC20.get_token_Name()