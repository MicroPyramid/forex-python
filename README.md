# forex-python

[![travis-ci](https://travis-ci.org/MicroPyramid/forex-python.svg?branch=master)](https://travis-ci.org/MicroPyramid/forex-python)
[![coveralls](https://coveralls.io/repos/github/MicroPyramid/forex-python/badge.svg?branch=master)](https://coveralls.io/github/MicroPyramid/forex-python?branch=master)
[![Code Health](https://landscape.io/github/MicroPyramid/forex-python/master/landscape.svg?style=flat)](https://landscape.io/github/MicroPyramid/forex-python/master)
[![pypi](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://pypi.python.org/pypi/forex-python)

**Forex Python** is a free library for foreign exchange rates and currency conversion, supporting Python 3.6 and above.

> **Note:** Install the latest version (`forex-python>=1.6`) to avoid `RatesNotAvailableError`.

## Features

- List all currency rates
- Bitcoin price for all currencies
- Convert amounts to and from Bitcoin
- Get historical rates (since 1999)
- Currency conversion (e.g., USD to INR)
- Currency symbols and names

## Currency Source

[theratesapi.com](https://theratesapi.com) provides current and historical foreign exchange rates published by the European Central Bank. Rates are updated daily at 3PM CET.

## Bitcoin Price Source

Bitcoin prices are updated every minute. For more information, visit [CoinDesk](http://www.coindesk.com).

## Installation

Install via pip:
```bash
pip install forex-python
```
Or clone the repository and install manually:
```bash
git clone https://github.com/MicroPyramid/forex-python.git
cd forex-python
python3 setup.py install
```

## Usage Examples

**Initialize the class:**
```python
from forex_python.converter import CurrencyRates
c = CurrencyRates()
```

**List all latest currency rates for "USD":**
```python
c.get_rates('USD')
# Example output: {'INR': 83.12, 'EUR': 0.92, ...}
```

**Get conversion rate from USD to INR:**
```python
c.get_rate('USD', 'INR')
# Example output: 83.12
```

**Convert amount from USD to INR:**
```python
c.convert('USD', 'INR', 10)
# Example output: 831.2
```

**Force use of Decimal:**
```python
from decimal import Decimal
c = CurrencyRates(force_decimal=True)
c.convert('USD', 'INR', Decimal('10.45'))
# Example output: 868.75
```

**Get latest Bitcoin price:**
```python
from forex_python.bitcoin import BtcConverter
b = BtcConverter()
b.get_latest_price('USD')
# Example output: 67000.0
```

**Convert amount to Bitcoins:**
```python
b.convert_to_btc(400, 'USD')
# Example output: 0.00597
```

**Get currency symbol using currency code:**
```python
from forex_python.converter import CurrencyCodes
codes = CurrencyCodes()
codes.get_symbol('GBP')
# Example output: '£'
```

For complete documentation, see the [forex-python docs](http://forex-python.readthedocs.org/en/latest/?badge=latest).

---

## Support & Feedback

- Found a bug? Please [open a GitHub issue](https://github.com/MicroPyramid/forex-python/issues).
- Need a new feature or custom development? [Contact us here](https://micropyramid.com/contact-us/).
- Visit our [Python Development Services](https://micropyramid.com/python-development-services/) page for more information.

---