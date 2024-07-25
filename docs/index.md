# SynarixAggregator Documentation

Welcome to the SynarixAggregator documentation! This guide provides an overview and detailed instructions for working with the SynarixAggregator project, a toolkit for interacting with the Synarix aggregator on EVMs.

## Get Started
The Synarix Aggregator project offers tools and classes for seamless integration with the Synarix aggregator. It includes:

- **`SynarixAggregatorModul`**: We call it SAM, An Modul that wrapp and manage subclasses of Synarix Aggregator.
    - **`IAC`**: Methods for interacting with the aggregator contract.
    - **`IERC20`**: Interface for interact with Token.
    - **`W3Utils`**: Management for Decimals and converting wei to ether or ether to wei, supports mutible formats.
    - **`CoreSettings`**: Configuration management for the user settings.

### Dependencies
- `web3`: For interacting with the Ethereum blockchain.
- `eth-abi`: For Ethereum ABI encoding/decoding

###  Installation
```bash
pip install SynarixAggregator
```

##### Import, initalize and test
```bash
from synarixaggregator import SynarixAggregatorModul

# Initialize the AggregatorInterface
SAM = SynarixAggregatorModul() 

# Interact with the aggregator modul
settings = SAM.getSettings()
print(settings)

# Interact with aggregator IERC20 submodul
balance = SAM.IERC20.get_token_balance(
 "0x0000022f6f742ca30bb7F309f53f619f36E826F2" # Synarix Deployer address
 )
print(balance)

# Interact with aggregator interface submodul
price = SAM.IAC.get_price()
print(price)
```



## Structure

- **[SynarixAggregatorModule (SAM)](Synarix_Aggregator_Module.md)**: 
  Detailed information about the `SynarixAggregatorModule` class, including its methods and attributes.

- **[CoreSettings (settings) Methods](settings_methods.md)**: 
  Overview of the `CoreSettings` class, including configuration management and validation.

- **[InterfaceAggregatorContract (IAC) Methods](aggregator_functions.md)**: 
  Comprehensive details on the methods provided by the `InterfaceAggregatorContract` class.

- **[Interface ERC20 (IERC20) Methods](ierc20_functions.md)**: 
  Comprehensive details on the methods provided by the `IERC20` class.

- **[w3Utils (w3Utils )Methods](w3Utils_functions.md)**: 
  Comprehensive details on the methods provided by the `W3Utils` class.



## Contributing
We welcome contributions to improve the SynarixAggregator project. 
#### To contribute:
##### 1. Fork the repository on GitHub.
##### 2. Create a new branch for your changes.
##### 3. Make your changes and commit them with clear messages.
##### 4. Push your branch to your forked repository.
##### 5. Submit a pull request with a description of your changes.

#### Please ensure your code adheres to the project's style guidelines and includes appropriate tests.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For questions, issues, or feedback, please reach out to:

Email: support@synarix.com

GitHub Issues: [Github Issues Page]

### Thank you for using SynarixAggregator! 
### We hope this documentation helps you effectively leverage our tools and integrate with Synarix.