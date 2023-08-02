import os
from decimal import Decimal

import requests
import simplejson as json


class RatesNotAvailableError(Exception):
    """
    Custom exception when https://theforexapi.com is down and not available for currency rates
    """
    pass


class DecimalFloatMismatchError(Exception):
    """
    A float has been supplied when force_decimal was set to True
    """
    pass


class Common:

    def __init__(self, force_decimal=False):
        self._force_decimal = force_decimal

    def _source_url(self):
        return None

    def _request(self, url, params):
        try:
            return requests.get(url, params=params)
        except:
            raise RatesNotAvailableError("Currency Rates Source Not Ready")

    def _get_date_string(self, date_obj):
        if date_obj is None:
            return 'latest'
        date_str = date_obj.strftime('%Y-%m-%d')
        return date_str

    def _decode_rates(self, response, use_decimal=False, date_str=None, base_cur=None):
        if self._force_decimal or use_decimal:
            decoded_data = json.loads(response.text, use_decimal=True)
        else:
            decoded_data = response.json()
        # if (date_str and date_str != 'latest' and date_str != decoded_data.get('date')):
        #     raise RatesNotAvailableError("Currency Rates Source Not Ready")
        if base_cur != None and base_cur != decoded_data['base']:
            raise RatesNotAvailableError("Currency Rates Source Not Ready")
        
        return decoded_data.get('rates', {})

    def _get_decoded_rate(
            self, response, dest_cur, use_decimal=False, date_str=None):
        return self._decode_rates(
            response, use_decimal=use_decimal, date_str=date_str).get(
            dest_cur, None)


class CurrencyRatesBase(Common):
    def get_rates(self, base_cur, date_obj=None):
        date_str = self._get_date_string(date_obj)
        payload = {'base': base_cur, 'rtype': 'fpy'}
        source_url = self._source_url() + date_str
        response = self._request(source_url, params=payload)
        if response.status_code == 200:
            rates = self._decode_rates(response, date_str=date_str)
            return rates
        raise RatesNotAvailableError("Currency Rates Source Not Ready")

    def get_rate(self, base_cur, dest_cur, date_obj=None, use_decimal=False):
        if base_cur == dest_cur:
            if use_decimal or self._force_decimal:
                return Decimal(1)
            return 1.
        date_str = self._get_date_string(date_obj)
        payload = {'base': base_cur, 'symbols': dest_cur, 'rtype': 'fpy'}
        source_url = self._source_url() + date_str
        response = self._request(source_url, params=payload)
        if response.status_code == 200:
            rate = self._get_decoded_rate(response, dest_cur, date_str=date_str)
            if not rate:
                raise RatesNotAvailableError("Currency Rate {0} => {1} not available for Date {2}".format(
                    base_cur, dest_cur, date_str))
            return rate
        raise RatesNotAvailableError("Currency Rates Source Not Ready")

    def convert(self, base_cur, dest_cur, amount, date_obj=None):
        use_decimal = False
        if isinstance(amount, Decimal):
            use_decimal = True
        elif self._force_decimal:
            raise DecimalFloatMismatchError("Decimal is forced. Amount must be Decimal")

        if base_cur == dest_cur:  # Return same amount if both base_cur, dest_cur are same
            return amount
        
        rate = self.get_rate(base_cur, dest_cur, date_obj=date_obj, use_decimal=use_decimal)

        return rate * amount

class CurrencyRatesForexAPI(CurrencyRatesBase):
    def _source_url(self):
        return "https://theforexapi.com/api/"

class CurrencyRatesExchangeRateHost(CurrencyRatesBase):
    def _source_url(self):
        return "https://api.exchangerate.host/"
    
    def get_rates(self, base_cur, date_obj=None):
        date_str = self._get_date_string(date_obj)
        payload = {'base': base_cur, 'rtype': 'fpy'}
        source_url = self._source_url() + date_str
        response = self._request(source_url, params=payload)
        if response.status_code == 200:
            rates = self._decode_rates(response,date_str=date_str, base_cur=base_cur)
            return rates
        raise RatesNotAvailableError("Currency Rates Source Not Ready")
    
class CurrencyRates(CurrencyRatesBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.providers = [
            CurrencyRatesForexAPI(*args, **kwargs),
            CurrencyRatesExchangeRateHost(*args, **kwargs)
        ]

    def get_rate(self, base_cur, dest_cur, date_obj=None, use_decimal=False):
        for provider in self.providers:
            try:
                return provider.get_rate(base_cur, dest_cur, date_obj=date_obj, use_decimal=use_decimal)
            except RatesNotAvailableError:
                continue
        raise RatesNotAvailableError("Rates Not Available For Any Provider")

    def get_rates(self, base_cur, date_obj=None):
        for provider in self.providers:
            try:
                return provider.get_rates(base_cur, date_obj=date_obj)
            except RatesNotAvailableError:
                continue
        raise RatesNotAvailableError("Rates Not Available For Any Provider")
    
_CURRENCY_FORMATTER = CurrencyRates()

get_rates = _CURRENCY_FORMATTER.get_rates
get_rate = _CURRENCY_FORMATTER.get_rate
convert = _CURRENCY_FORMATTER.convert


class CurrencyCodes:

    def __init__(self):
        self.__currency_data = None

    @property
    def _currency_data(self):
        if self.__currency_data is None:
            file_path = os.path.dirname(os.path.abspath(__file__))
            with open(file_path + '/raw_data/currencies.json') as f:
                self.__currency_data = json.loads(f.read())
        return self.__currency_data

    def _get_data(self, currency_code):
        currency_dict = next((item for item in self._currency_data if item["cc"] == currency_code), None)
        return currency_dict

    def _get_data_from_symbol(self, symbol):
        currency_dict = next((item for item in self._currency_data if item["symbol"] == symbol), None)
        return currency_dict

    def get_symbol(self, currency_code):
        currency_dict = self._get_data(currency_code)
        if currency_dict:
            return currency_dict.get('symbol')
        return None

    def get_currency_name(self, currency_code):
        currency_dict = self._get_data(currency_code)
        if currency_dict:
            return currency_dict.get('name')
        return None

    def get_currency_code_from_symbol(self, symbol):
        currency_dict = self._get_data_from_symbol(symbol)
        if currency_dict:
            return currency_dict.get('cc')
        return None


_CURRENCY_CODES = CurrencyCodes()

get_symbol = _CURRENCY_CODES.get_symbol
get_currency_name = _CURRENCY_CODES.get_currency_name
get_currency_code_from_symbol = _CURRENCY_CODES.get_currency_code_from_symbol
