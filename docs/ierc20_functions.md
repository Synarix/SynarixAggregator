# `IERC20` Class Documentation

## Overview

The `IERC20` class provides an interface for interacting with ERC-20 tokens using the Web3.py library. It includes methods for checking token balances, allowances, and for approving token transfers.

```bash
from pysynarixaggregator import SynarixAggregatorInterface
#Initalize SynarixAggregatorInterface
aggregator = SynarixAggregatorInterface()

# use SynarixAggregatorInterface().IERC20.<methods>
print(aggregator.IERC20.get_token_address())

```
## Methods


### `get_token_balance(address)`

Fetches the balance of the given address in the token.

**Parameters:**

- **`address`**: The address to check the balance for.

**Returns:**

- The token balance of the specified address.

### `get_token_allowance(spender)`

Fetches the allowance of the token for a specified spender.

**Parameters:**

- **`spender`**: The address of the spender.

**Returns:**

- The amount of token allowed for the spender.

### `get_token_address()`

Gets the address of the token contract.

**Returns:**

- The token contract address.

### `get_token_decimals()`

Fetches the number of decimal places the token uses.

**Returns:**

- The number of decimal places.

### `get_token_Name()`

Fetches the name of the token.

**Returns:**

- The token name.

### `get_token_Symbol()`

Fetches the symbol of the token.

**Returns:**

- The token symbol.

### `get_token_balance_(address)`

Fetches the raw balance of the token for the given address.

**Parameters:**

- **`address`**: The address to check the balance for.

**Returns:**

- The raw balance of the token.

### `get_token_allowance(spender)`

Fetches the raw allowance of the token for a specified spender.

**Parameters:**

- **`spender`**: The address of the spender.

**Returns:**

- The raw amount of token allowed for the spender.

### `is_approved(spender, amountIn)`

Checks if the token amount is already approved for a spender.

**Parameters:**

- **`spender`**: The address of the spender.
- **`amountIn`**: The amount to check.

**Returns:**

- `True` if the amount is approved, otherwise `False`.

### `approve(spender, amountIn)`

Approves a spender to spend an amount of tokens on behalf of the user.

**Parameters:**

- **`spender`**: The address of the spender.
- **`amountIn`**: The amount to approve.

**Returns:**

- A tuple of `(success, transaction_hash, gas_used)`:
  - **`success`**: `True` if the transaction was successful, `False` otherwise.
  - **`transaction_hash`**: The transaction hash of the approval transaction.
  - **`gas_used`**: The gas used for the transaction.

## Conclusion

This documentation outlines the purpose and functionality of each method and provides clear guidance on how to use the `IERC20` class. Adjust the content as needed based on additional context or specific requirements of your project.
