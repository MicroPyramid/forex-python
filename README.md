forex-python
============
[![Build Status](https://travis-ci.org/MicroPyramid/forex-python.svg?branch=master)](https://travis-ci.org/MicroPyramid/forex-python)
[![Coverage Status](https://coveralls.io/repos/github/MicroPyramid/forex-python/badge.svg?branch=master)](https://coveralls.io/github/MicroPyramid/forex-python?branch=master)
[![Code Health](https://landscape.io/github/MicroPyramid/forex-python/master/landscape.svg?style=plastic)](https://landscape.io/github/MicroPyramid/forex-python/master)

Free Foreign exchange rates and currency conversion.

Features:
---------
- List all currency rates.
- Get historical rates for any day since 1999.
- Conversion rate for one Currency(ex; USD to INR).
- Convert amount from one currency to other.('USD 10$' to INR)

Currency Source:
---------------
Fixer.io is a free API for current and historical foreign exchange rates published by European Central Bank.
The rates are updated daily 3PM CET.

Installation:
------------

Install using python package
```
$ pip install forex-python
```

Or directly cloning the repo:
```
$ python setup.py install
```

Examples:
------------------

Initialize class
```python
>>> from forex_python.converter import CurrencyRates
>>> c = CurrencyRates()
```

list all latest currency rates for "USD"
```python
>>> c.get_rates('USD')
{u'IDR': 13625.0, u'BGN': 1.7433, u'ILS': 3.8794, u'GBP': 0.68641, u'DKK': 6.6289, u'CAD': 1.3106, u'JPY': 110.36, u'HUF': 282.36, u'RON': 4.0162, u'MYR': 4.081, u'SEK': 8.3419, u'SGD': 1.3815, u'HKD': 7.7673, u'AUD': 1.3833, u'CHF': 0.99144, u'KRW': 1187.3, u'CNY': 6.5475, u'TRY': 2.9839, u'HRK': 6.6731, u'NZD': 1.4777, u'THB': 35.73, u'EUR': 0.89135, u'NOK': 8.3212, u'RUB': 66.774, u'INR': 67.473, u'MXN': 18.41, u'CZK': 24.089, u'BRL': 3.5473, u'PLN': 3.94, u'PHP': 46.775, u'ZAR': 15.747}
```

Get Conversion rate from USD to INR
```python
>>> c.get_rate('USD', 'INR')
67.473
```

Convert amount from USD to INR:
```python
>>> c.convert('USD', 'INR', 10)
674.73
```

Convert amount from USD to INR based on 2010-03-01 rates
```python
>>> import datetime
>>> date_obj = datetime.datetime.strptime('2010-05-10', "%Y-%m-%d").date()
>>> c.convert('EUR', 'USD', 10, date_obj)
12.969
```

RatesNotAvailableError for invalid currency codes and missing currency code from source:
```python
    >>> c.get_rate('XYZ', 'INR')
    Traceback (most recent call last):
    RatesNotAvailableError: Currency XYZ => INR rate not available for Date latest.
```

Compleate [Documentation](http://forex-python.readthedocs.org/en/latest/?badge=latest)

We welcome your feedback and support. found bug raise github issue.

