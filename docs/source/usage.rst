Usage Examples:
===============

Currency Rates
--------------
1. list all latest currency rates for "USD"::
     >>> from forex_python.converter import CurrencyRates
     >>> c = CurrencyRates()
     >>> c.get_rates('USD')   # you can directly call get_rates('USD')
     {u'IDR': 13625.0, u'BGN': 1.7433, u'ILS': 3.8794, u'GBP': 0.68641, u'DKK': 6.6289, u'CAD': 1.3106, u'JPY': 110.36, u'HUF': 282.36, u'RON': 4.0162, u'MYR': 4.081, u'SEK': 8.3419, u'SGD': 1.3815, u'HKD': 7.7673, u'AUD': 1.3833, u'CHF': 0.99144, u'KRW': 1187.3, u'CNY': 6.5475, u'TRY': 2.9839, u'HRK': 6.6731, u'NZD': 1.4777, u'THB': 35.73, u'EUR': 0.89135, u'NOK': 8.3212, u'RUB': 66.774, u'INR': 67.473, u'MXN': 18.41, u'CZK': 24.089, u'BRL': 3.5473, u'PLN': 3.94, u'PHP': 46.775, u'ZAR': 15.747}

2. List all Currency rates for "USD" on 2012-09-05::
     >>> date_obj
     datetime.datetime(2014, 5, 23, 18, 36, 28, 151012)
     >>> c.get_rates('USD', date_obj)  # same as get_rates('USD', date_obj)
     {u'IDR': 11612.0, u'BGN': 1.4349, u'ILS': 3.4861, u'GBP': 0.5938, u'DKK': 5.4762, u'CAD': 1.0901, u'JPY': 101.92, u'HUF': 222.66, u'RON': 3.2359, u'MYR': 3.2101, u'EUR': 0.73368, u'SEK': 6.6471, u'SGD': 1.2527, u'HKD': 7.7519, u'AUD': 1.0845, u'CHF': 0.89582, u'KRW': 1024.9, u'CNY': 6.2377, u'TRY': 2.0888, u'HRK': 5.5751, u'NZD': 1.1707, u'THB': 32.6, u'LTL': 2.5332, u'NOK': 5.9652, u'RUB': 34.122, u'INR': 58.509, u'MXN': 12.893, u'CZK': 20.131, u'BRL': 2.2178, u'PLN': 3.0544, u'PHP': 43.721, u'ZAR': 10.356}

3. Get conversion rate from USD to INR::
     >>> c.get_rate('USD', 'INR')    # same as get_rate('USD', 'INR')
     67.473  # return type float

4. Get conversion rate from USD to INR on 2014-05-23::
     >>> date_obj
     datetime.datetime(2014, 5, 23, 18, 36, 28, 151012)
     >>> c.get_rate('USD', 'INR', date_obj)   # get_rate('USD', 'INR', date_obj)
     58.509

5. Convert amount from USD to INR::
     >>> c.convert('USD', 'INR', 10)  # convert('USD', 'INR', 10)
     674.73

6. Convert amount from USD to INR based on 2014-05-23 exchange rates::
     >>> date_obj
     datetime.datetime(2014, 5, 23, 18, 36, 28, 151012)
     >>> c.convert('USD', 'INR', 10, date_obj)
     585.09

7. Force use of Decimal::
    >>> from forex_python.converter import CurrencyRates
    >>> c = CurrencyRates(force_decimal=True)
    >>> c.convert('USD', 'INR', Decimal('10.45'))
    Decimal('705.09')
    >>> c.convert('USD', 'INR', 10)
    DecimalFloatMismatchError: convert requires amount parameter is of type Decimal when use_decimal=True

8. Detect use of Decimal::
    >>> from forex_python.converter import CurrencyRates
    >>> c = CurrencyRates()
    >>> c.convert('USD', 'INR', Decimal('10.45'))
    Decimal('705.09')
    >>> c.convert('USD', 'INR', 10)
    674.73


Bitcoin Prices:
---------------
1. Get latest price of one Bitcoin::
     >>> from forex_python.bitcoin import BtcConverter
     >>> b = BtcConverter()   # add "force_decimal=True" parmeter to get Decimal rates
     >>> b.get_latest_price('EUR')   # you can directly call get_latest_price('EUR')
     476.5225  # return type float

2. Get price of Bitcoin based on previous date::
     >>> date_obj
     datetime.datetime(2016, 5, 18, 19, 39, 36, 815417)
     >>> b.get_previous_price('USD', date_obj)  # get_previous_price('USD', date_obj)
     453.378

3. Convert Amount to Bitcoin::
     >>> b.convert_to_btc(5000, 'USD')  # convert_to_btc(5000, 'USD')
     9.36345369116708

4. Convert Amount to Bitcoin based on previous date prices::
     >>> date_obj
     datetime.datetime(2016, 5, 18, 19, 39, 36, 815417)
     >>> b.convert_to_btc_on(5000, 'USD', date_obj)   # convert_to_btc_on(5000, 'USD', date_obj)
     11.028325150316071

5. Convert Bitcoin to valid currency amount based on latest price::
     >>> b.convert_btc_to_cur(1.25, 'USD')   # convert_btc_to_cur(1.25, 'USD')
     668.1012499999999

6. Convert Bitcoin to valid currency amount based on previous date price::
     >>> date_obj
     datetime.datetime(2016, 5, 18, 19, 39, 36, 815417)
     >>> b.convert_btc_to_cur_on(1.25, 'EUR', date_obj)
     504.23625000000004

7. Get list of prices list for given date range::
     >>> start_date
     datetime.datetime(2016, 5, 18, 19, 39, 36, 815417)
     >>> end_date
     datetime.datetime(2016, 5, 23, 19, 39, 36, 815417)
     >>> b.get_previous_price_list('INR', start_date, end_date)  # get_previous_price_list('INR', start_date, end_date)
     {u'2016-05-19': 29371.7579, u'2016-05-18': 30402.3169, u'2016-05-22': 29586.3631, u'2016-05-23': 29925.3272, u'2016-05-20': 29864.0256, u'2016-05-21': 29884.7449}

8. Force use of Decimal::
     >>> from forex_python.bitcoin import BtcConverter
     >>> b = BtcConverter(force_decimal=True)
     >>> b.get_latest_price('EUR')   # you can directly call get_latest_price('EUR')
     Decimal('942.245000000000004547')  # return type Decimal

9. Get Bitcoin symbol::
     >>> print(b.get_symbol())  # get_btc_symbol()
     ฿

Currency Symbols & Codes
-------------------------
1. Get currency symbol using currency code::
     >>> from forex_python.converter import CurrencyCodes
     >>> c = CurrencyCodes()
     >>> c.get_symbol('GBP')
     u'\xa3'
     >>> print c.get_symbol('GBP')
     £
     >>> print c.get_symbol('EUR')
     €

2. Get currency name using currency code::
     >>> c.get_currency_name('EUR')
     u'European Euro'
     >>> c.get_currency_name('INR')
     u'Indian Rupee'
