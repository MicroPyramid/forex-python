import os
from decimal import Decimal

import requests
import simplejson as json


class RatesNotAvailableError(Exception):
    """
    Custome Exception when https://ratesapi.io is Down and not available for currency rates
    """
    pass


class DecimalFloatMismatchError(Exception):
    """
    A float has been supplied when force_decimal was set to True
    """
    pass


class Common:

    def __init__(self, force_decimal=False, use_https=False):
        self._force_decimal = force_decimal
        self.protocol = "https://" if use_https else "http://"

    def _source_url(self):
        return self.protocol + "api.exchangeratesapi.io/v1/"

    def _get_date_string(self, date_obj):
        if date_obj is None:
            return 'latest'
        date_str = date_obj.strftime('%Y-%m-%d')
        return date_str

    def _decode_rates(self, response, use_decimal=False):
        if self._force_decimal or use_decimal:
            decoded_data = json.loads(response.text, use_decimal=True).get('rates', {})
        else:
            decoded_data = response.json().get('rates', {})
        return decoded_data

    def _get_decoded_rate(self, response, dest_cur, use_decimal=False):
        return self._decode_rates(response, use_decimal=use_decimal).get(dest_cur, None)


class CurrencyRates(Common):
    def __init__(self, access_key, use_https=False, force_decimal=False):
        super().__init__(force_decimal, use_https)
        self.access_key = access_key

    def get_rates(self, base_cur, date_obj=None):
        date_str = self._get_date_string(date_obj)
        source_url = self._source_url() + date_str + "?access_key=%s" % self.access_key
        response = requests.get(source_url)
        if response.status_code == 200:
            rates = self._decode_rates(response)
            return rates
        raise RatesNotAvailableError("Currency Rates Source Not Ready")

    def get_rate(self, base_cur, dest_cur, date_obj=None):
        if base_cur == dest_cur:
            if self._force_decimal:
                return Decimal(1)
            return 1.
        date_str = self._get_date_string(date_obj)
        source_url = self._source_url() + date_str + "?access_key=%s" % self.access_key
        response = requests.get(source_url)
        if response.status_code == 200:
            rate = self._get_decoded_rate(response, dest_cur)
            if not rate:
                raise RatesNotAvailableError("Currency Rate {0} => {1} not available for Date {2}".format(
                    base_cur, dest_cur, date_str))
            return rate
        raise RatesNotAvailableError("Currency Rates Source Not Ready")

    def convert(self, base_cur, dest_cur, amount, date_obj=None):
        if isinstance(amount, Decimal):
            use_decimal = True
        else:
            use_decimal = self._force_decimal

        if base_cur == dest_cur:  # Return same amount if both base_cur, dest_cur are same
            if use_decimal:
                return Decimal(amount)
            return float(amount)

        date_str = self._get_date_string(date_obj)
        source_url = self._source_url() + date_str + "?access_key=%s" % self.access_key
        response = requests.get(source_url)
        if response.status_code == 200:
            rate = self._get_decoded_rate(response, dest_cur, use_decimal=use_decimal)
            if not rate:
                raise RatesNotAvailableError("Currency {0} => {1} rate not available for Date {2}.".format(
                    source_url, dest_cur, date_str))
            try:
                converted_amount = rate * amount
                return converted_amount
            except TypeError:
                raise DecimalFloatMismatchError(
                    "convert requires amount parameter is of type Decimal when force_decimal=True")
        raise RatesNotAvailableError("Currency Rates Source Not Ready")

# Please add your access key here
_CURRENCY_FORMATTER = CurrencyRates("your_access_key")

get_rates = _CURRENCY_FORMATTER.get_rates
get_rate = _CURRENCY_FORMATTER.get_rate
convert = _CURRENCY_FORMATTER.convert


class CurrencyCodes:

    def __init__(self):
        pass

    def _get_data(self, currency_code):
        file_path = os.path.dirname(os.path.abspath(__file__))
        with open(file_path + '/raw_data/currencies.json') as f:
            currency_data = json.loads(f.read())
        currency_dict = next((item for item in currency_data if item["cc"] == currency_code), None)
        return currency_dict

    def _get_data_from_symbol(self, symbol):
        file_path = os.path.dirname(os.path.abspath(__file__))
        with open(file_path + '/raw_data/currencies.json') as f:
            currency_data = json.loads(f.read())
        currency_dict = next((item for item in currency_data if item["symbol"] == symbol), None)
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
