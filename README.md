forex-python
============

Foreign exchange rates and currency conversion.

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

.. code-block:: bash

 $ pip install forex-python

Or directly cloning the repo:

.. code-block:: bash

  $ python setup.py install

Examples:
------------------

Initialize class

.. code-block:: python

    >>> from forex_python.converter import CurrencyRates
    >>> c = CurrencyRates()

list all latest currency rates for "USD"

.. code-block:: python

    >>> c.get_rates('USD')
    {'EUR':19.22}

Get Conversion rate from USD to INR

.. code-block:: python

    >>> c.get_rate('USD', 'INR')
    67.32

Convert amount from USD to INR:
.. code-block:: python

    >>> c.convert('USD', 'INR', 10)
    673.25

Convert amount from USD to INR based on 2010-03-01 rates

.. code-block:: python

    >>> c.convert(100, 'EUR', 'USD', 10, "2010-03-01")
    632.60

RatesNotAvailableError for invalid currency codes and missing currency code from source:

.. code-block:: python

    >>> c.get_rate('XYZ', 'INR')
    Traceback (most recent call last):
    RatesNotAvailableError: Currency XYZ => INR rate not available for Date latest.

Compleate `documentation`_

We welcome your feedback and support. found bug raise github issue.

.. _documentation: http://forex-python.readthedocs.org/en/latest/?badge=latest
