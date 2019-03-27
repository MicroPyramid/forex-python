forex-python
============

.. image:: https://travis-ci.org/MicroPyramid/forex-python.svg?branch=master
   :target: https://travis-ci.org/MicroPyramid/forex-python
   :alt: travis-ci

.. image:: https://coveralls.io/repos/github/MicroPyramid/forex-python/badge.svg?branch=master
   :target: https://coveralls.io/github/MicroPyramid/forex-python?branch=master
   :alt: coveralls

.. image:: https://landscape.io/github/MicroPyramid/forex-python/master/landscape.svg?style=flat
   :target: https://landscape.io/github/MicroPyramid/forex-python/master
   :alt: Code Health

.. image:: https://img.shields.io/badge/python-2.7%2C%203.3%2C%203.4%2C%203.5-blue.svg
    :target: https://pypi.python.org/pypi/forex-python
	:alt: pypi

Forex Python is a Free Foreign exchange rates and currency conversion.

**Note: Install latest forex-python==1.1 to avoid RatesNotAvailableError**

Features:
---------
- List all currency rates.
- BitCoin price for all currencies.
- Converting amount to BitCoins.
- Get historical rates for any day since 1999.
- Conversion rate for one currency(ex; USD to INR).
- Convert amount from one currency to other.('USD 10$' to INR).
- Currency symbols.
- Currency names.

Currency Source:
-----------------

https://ratesapi.io is a free API for current and historical foreign exchange rates published by European Central Bank.
The rates are updated daily 3PM CET.

BitCoin Price Source:
---------------------
Bitcoin prices calculated every minute. For more information visit [CoinDesk API](http://www.coindesk.com/api/).

Installation
--------------

- Install using python package

	.. code-block:: python

			pip install forex-python

				Or directly cloning the repo:

			python setup.py install

Usage Examples:
------------------

- Initialize class

	.. code-block:: python

			python
			>>> from forex_python.converter import CurrencyRates
			>>> c = CurrencyRates()

- list all latest currency rates for "USD"

	.. code-block:: python

			python
			>>> c.get_rates('USD')
			{u'IDR': 13625.0, u'BGN': 1.7433, u'ILS': 3.8794, u'GBP': 0.68641, u'DKK': 6.6289, u'CAD': 1.3106, u'JPY': 110.36, u'HUF': 282.36, u'RON': 4.0162, u'MYR': 4.081, u'SEK': 8.3419, u'SGD': 1.3815, u'HKD': 7.7673, u'AUD': 1.3833, u'CHF': 0.99144, u'KRW': 1187.3, u'CNY': 6.5475, u'TRY': 2.9839, u'HRK': 6.6731, u'NZD': 1.4777, u'THB': 35.73, u'EUR': 0.89135, u'NOK': 8.3212, u'RUB': 66.774, u'INR': 67.473, u'MXN': 18.41, u'CZK': 24.089, u'BRL': 3.5473, u'PLN': 3.94, u'PHP': 46.775, u'ZAR': 15.747}

- Get conversion rate from USD to INR

	.. code-block:: python

			python
			>>> c.get_rate('USD', 'INR')
			67.473

- Convert amount from USD to INR

	.. code-block:: python

			python
			>>> c.convert('USD', 'INR', 10)
			674.73

- Force use of Decimal

	.. code-block:: python

			python
			>>> from forex_python.converter import CurrencyRates
			>>> c = CurrencyRates(force_decimal=True)
			>>> c.convert('USD', 'INR', Decimal('10.45'))
			705.09
			>>> c.convert('USD', 'INR', 10)
			DecimalFloatMismatchError: convert requires amount parameter is of type Decimal when use_decimal=True

- Detect use of Decimal

	.. code-block:: python

			python
			>>> from forex_python.converter import CurrencyRates
			>>> c = CurrencyRates()
			>>> c.convert('USD', 'INR', Decimal('10.45'))
			705.09
			>>> c.convert('USD', 'INR', 10)
			674.73

- Get latest Bitcoin price.

	.. code-block:: python

			python
			>>> from forex_python.bitcoin import BtcConverter
			>>> b = BtcConverter() # force_decimal=True to get Decimal rates
			>>> b.get_latest_price('USD')
			533.913


- Convert Amount to Bitcoins based on latest exchange price.

	.. code-block:: python

			python
			>>> b.convert_to_btc(400, 'USD')
			0.7492699301118473


- Get currency symbol using currency code

	.. code-block:: python

			python
			>>> from forex_python.converter import CurrencyCodes
			>>> c = CurrencyCodes()
			>>> print c.get_symbol('GBP')
			£


You can view the complete `Documentation Here`_

Visit our Python Development page `Here`_

We welcome your feedback and support, raise `github ticket`_ if you want to report a bug. Need new features? `Contact us here`_

.. _contact us here: https://micropyramid.com/contact-us/
.. _github ticket: https://github.com/MicroPyramid/forex-python/issues
.. _Documentation Here: http://forex-python.readthedocs.org/en/latest/?badge=latest
.. _Here: https://micropyramid.com/python-development-services/
