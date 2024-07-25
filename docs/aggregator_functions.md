# `InterfaceAggregatorContract` Class Documentation

## Overview

The `InterfaceAggregatorContract` (IAC) class provides methods for interacting with the Synarix Aggregator smart contract, including functions for swapping tokens, fetching prices, and obtaining token information. It supports multiple versions of the aggregator protocol (V2 and V3) and integrates with Ethereum using Web3.py.



## Methods

### `getAmountsOutV3(pools, path, amountIn)`

**Parameters:**

- **`pools`**: List of liquidity pool addresses.
- **`path`**: List of token addresses representing the swap path.
- **`amountIn`**: Amount of input tokens.

**Returns:**

- The output amounts for the given inputs and pools.

**Example:**
```python
pools = ['0xPoolAddress1', '0xPoolAddress2']
path = ['0xTokenInAddress0', '0xTokenOutAddress1','0xTokenOutAddress1', ]
amountIn = 1_000_000_000_000_000_000  # 1 ETH in Wei
output_amounts = SAM.IAC.getAmountsOutV3(pools, path, amountIn)
print(output_amounts)  # Example: [1_000_000_000_000_000_000, 2_000_000_000_000_000_000]
```

### `getAmountsOutV2(amountIn, path, dexPath)`

**Parameters:**
- **`amountIn`**: Amount of input tokens.
- **`path`**: List of token addresses representing the swap path.
- **`dexPath`**: List of DEX identifiers.

**Returns:**

- The output amounts for the given inputs and paths.

**Example:**
```python
amountIn = 1_000_000_000_000_000_000  # 1 ETH in Wei
path = ['0xTokenInAddress', '0xTokenOutAddress']
dexPath = [0, 1]  # Example DEX identifiers

output_amounts = SAM.IAC.getAmountsOutV2(amountIn, path, dexPath)
print(output_amounts)  # Example: [1_000_000_000_000_000_000, 2_000_000_000_000_000_000]
```

### `getUSDPrice_()`

**Returns:**
- The USD price of the token in its smallest unit (wei).

**Details:**
- Returns the price of the token in USD from the aggregator contract in wei.

**Example:**
```python
usd_price = SAM.IAC.getUSDPrice_()
print(usd_price)  # Example: 300_000_000_000 (USD price in smallest unit) price and liquidity always 18 decimals
```
### `getUSDPrice()`

**Returns:**
- The USD price of the token in normal unit. (ether)

**Details:**
- Returns the price of the token in USD from the aggregator contract in ether.

**Example:**
```python
usd_price_ether = SAM.IAC.getUSDPrice()
print(usd_price_ether)  # Example: 0.001 (USD price in Ether) 
```

### `getWBNBPrice_()`

**Returns:**

- The USD price of WBNB in its smallest unit (wei).

**Details:**
- Returns the price of WBNB in USD from the aggregator contract in wei.

**Example:**
```python
wbnb_price = SAM.IAC.getWBNBPrice_()
print(wbnb_price)  # Example: 400_000_000_000 (USD price in smallest unit)

```



### `getWBNBPrice()`

**Returns:**

- The USD price of WBNB in Ether.

**Details:**
- Returns the price of WBNB in USD from the aggregator contract in Ether.

**Example:**
```python
wbnb_price_ether = SAM.IAC.getWBNBPrice()
print(wbnb_price_ether)  # Example: 0.0025 (USD price in Ether)
```

### `getAmountsOutTokenToBNB_(inputAmount: int)`

**Parameters:**

- **`inputAmount`**: Amount of input tokens.

**Returns:**

- The output amounts of WBNB for the given input tokens.

**Example:**
```python

```
### `getAmountsOutBNBToToken_(inputAmount: int)`

**Parameters:**

- **`inputAmount`**: Amount of input WBNB.

**Returns:**

- The output amounts of the token for the given input WBNB.

### `getAmountsOutTokenToToken_(tokenIn, tokenOut, inputAmount: int)`

**Parameters:**

- **`tokenIn`**: Address of the input token.
- **`tokenOut`**: Address of the output token.
- **`inputAmount`**: Amount of input tokens.

**Returns:**

- The output amounts of the `tokenOut` for the given input tokens.

### `getLiquidityUSD_(isTokenIn)`

**Parameters:**

- **`isTokenIn`**: Boolean indicating if the token is in the liquidity pair.

**Returns:**

- The liquidity value in USD for the given token.

### `getLiquidityUSD(isTokenIn)`

**Parameters:**

- **`isTokenIn`**: Boolean indicating if the token is in the liquidity pair.

**Returns:**

- The liquidity value in USD for the given token, converted from Wei.

### `getSwapProtocollVersion()`

**Returns:**

- The version of the swap protocol used by the aggregator contract.

### `getTokenInfos()`

**Returns:**

- Tuple containing buy tax, sell tax, and honeypot status of the token.

**Details:**

- Retrieves information about the token, including buy and sell taxes and whether it is a honeypot.

### `getWalletTokenDATA(tokenList)`

**Parameters:**

- **`tokenList`**: List of token addresses.

**Returns:**

- Tuple containing token balances, decimals, prices, versions, and addresses for the specified tokens.

### `getETHtoTokenPathV3()`

**Returns:**

- Path and other details for swapping ETH to the token using V3.

### `getTokentoETHPathV3()`

**Returns:**

- Path and other details for swapping the token to ETH using V3.

### `getTokentoTokenPathV3(tokenIn, tokenOut)`

**Parameters:**

- **`tokenIn`**: Address of the input token.
- **`tokenOut`**: Address of the output token.

**Returns:**

- Path and other details for swapping `tokenIn` to `tokenOut` using V3.

### `getETHtoTokenPathV2()`

**Returns:**

- Path and other details for swapping ETH to the token using V2.

### `getTokentoETHPathV2()`

**Returns:**

- Path and other details for swapping the token to ETH using V2.

### `getTokentoTokenPathV2(tokenIn, tokenOut)`

**Parameters:**

- **`tokenIn`**: Address of the input token.
- **`tokenOut`**: Address of the output token.

**Returns:**

- Path and other details for swapping `tokenIn` to `tokenOut` using V2.

### `getBNBBalance()`

**Returns:**

- The BNB balance of the user’s address.

### `TestSwapETHtoToken(inputAmount: float)`

**Parameters:**

- **`inputAmount`**: Amount of ETH to swap.

**Returns:**

- Boolean indicating whether the swap test was successful.

### `TestSwapFromETHtoTokenV2(inputAmount: int)`

**Parameters:**

- **`inputAmount`**: Amount of ETH to swap.

**Returns:**

- Boolean indicating whether the swap test was successful using V2.

### `TestSwapFromETHtoTokenV3(inputAmount: int)`

**Parameters:**

- **`inputAmount`**: Amount of ETH to swap.

**Returns:**

- Boolean indicating whether the swap test was successful using V3.

### `SwapETHtoToken(inputAmount: float, trys: int)`

**Parameters:**

- **`inputAmount`**: Amount of ETH to swap.
- **`trys`**: Number of retry attempts.

**Returns:**

- Tuple containing a Boolean indicating success and the transaction hash.

### `SwapFromETHtoTokenV2(inputAmount: int)`

**Parameters:**

- **`inputAmount`**: Amount of ETH to swap.

**Returns:**

- Tuple containing a Boolean indicating success, the transaction hash, and gas used.

### `SwapFromETHtoTokenV3(inputAmount: int)`

**Parameters:**

- **`inputAmount`**: Amount of ETH to swap.

**Returns:**

- Tuple containing a Boolean indicating success, the transaction hash, and gas used.

### `SwapTokentoETH(inputAmount: float, trys: int = 1)`

**Parameters:**

- **`inputAmount`**: Amount of tokens to swap.
- **`trys`**: Number of retry attempts.

**Returns:**

- Tuple containing a Boolean indicating success and the transaction hash.

### `SwapFromTokentoETHV3(inputAmount: int)`

**Parameters:**

- **`inputAmount`**: Amount of tokens to swap.

**Returns:**

- Tuple containing a Boolean indicating success, the transaction hash, and gas used.

### `SwapFromTokentoTokenV3(tokenIn, tokenOut, inputAmount: int)`

**Parameters:**

- **`tokenIn`**: Address of the input token.
- **`tokenOut`**: Address of the output token.
- **`inputAmount`**: Amount of input tokens.

**Returns:**

- Tuple containing a Boolean indicating success, the transaction hash, and gas used.

### `SwapFromTokentoETHV2(inputAmount: int, trys: int = 1)`

**Parameters:**

- **`inputAmount`**: Amount of tokens to swap.
- **`trys`**: Number of retry attempts.

**Returns:**

- Tuple containing a Boolean indicating success, the transaction hash, and gas used.

### `SwapFromTokentoTokenV2(tokenIn, tokenOut, inputAmount: int, trys: int = 1)`

**Parameters:**

- **`tokenIn`**: Address of the input token.
- **`tokenOut`**: Address of the output token.
- **`inputAmount`**: Amount of input tokens.
- **`trys`**: Number of retry attempts.

**Returns:**

- Tuple containing a Boolean indicating success, the transaction hash, and gas used.

