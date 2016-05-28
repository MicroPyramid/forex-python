Usage Examples:
===============

Currency Rates
--------------
1. list all latest currency rates for "USD"::
     >>> from forex_python.converter import CurrencyRates
     >>> c = CurrencyRates()
     >>> c.get_rates('USD')
     {u'IDR': 13625.0, u'BGN': 1.7433, u'ILS': 3.8794, u'GBP': 0.68641, u'DKK': 6.6289, u'CAD': 1.3106, u'JPY': 110.36, u'HUF': 282.36, u'RON': 4.0162, u'MYR': 4.081, u'SEK': 8.3419, u'SGD': 1.3815, u'HKD': 7.7673, u'AUD': 1.3833, u'CHF': 0.99144, u'KRW': 1187.3, u'CNY': 6.5475, u'TRY': 2.9839, u'HRK': 6.6731, u'NZD': 1.4777, u'THB': 35.73, u'EUR': 0.89135, u'NOK': 8.3212, u'RUB': 66.774, u'INR': 67.473, u'MXN': 18.41, u'CZK': 24.089, u'BRL': 3.5473, u'PLN': 3.94, u'PHP': 46.775, u'ZAR': 15.747}

2. List all Currency rates for "USD" on 2012-09-05::
     >>> date_obj
     datetime.datetime(2014, 5, 23, 18, 36, 28, 151012)
     >>> c.get_rates('USD', date_obj)
     {u'IDR': 11612.0, u'BGN': 1.4349, u'ILS': 3.4861, u'GBP': 0.5938, u'DKK': 5.4762, u'CAD': 1.0901, u'JPY': 101.92, u'HUF': 222.66, u'RON': 3.2359, u'MYR': 3.2101, u'EUR': 0.73368, u'SEK': 6.6471, u'SGD': 1.2527, u'HKD': 7.7519, u'AUD': 1.0845, u'CHF': 0.89582, u'KRW': 1024.9, u'CNY': 6.2377, u'TRY': 2.0888, u'HRK': 5.5751, u'NZD': 1.1707, u'THB': 32.6, u'LTL': 2.5332, u'NOK': 5.9652, u'RUB': 34.122, u'INR': 58.509, u'MXN': 12.893, u'CZK': 20.131, u'BRL': 2.2178, u'PLN': 3.0544, u'PHP': 43.721, u'ZAR': 10.356}

3. Get conversion rate from USD to INR::
     >>> c.get_rate('USD', 'INR')
     67.473

4. Get conversion rate from USD to INR on 2014-05-23::
     >>> date_obj
     datetime.datetime(2014, 5, 23, 18, 36, 28, 151012)
     >>> c.get_rate('USD', 'INR', date_obj)
     58.509

5. Convert amount from USD to INR::
     >>> c.convert('USD', 'INR', 10)
     674.73

6. Convert amount from USD to INR based on 2014-05-23 exchange rates::
     >>> date_obj
     datetime.datetime(2014, 5, 23, 18, 36, 28, 151012)
     >>> c.convert('USD', 'INR', 10, date_obj)
     585.09

Currency Symboles & Codes
-------------------------
1. Get Currency symbol Using currency code::
     >>> from forex_python.converter import CurrencyCodes
     >>> c = CurrencyCodes()
     >>> c.get_symbol('GBP')
     u'\xa3'
     >>> print c.get_symbol('GBP')
     £
     >>> print c.get_symbol('EUR')
     €

2. Get Currency Name using currency code::
     >>> c.get_currency_name('EUR')
     u'European Euro'
     >>> c.get_currency_name('INR')
     u'Indian rupee'



