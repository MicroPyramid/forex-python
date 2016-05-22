import requests


class RatesNotAvailableError(Exception):
    """
    Custome Exception when http://fixer.io/ is Down are not available for currency rates
    """
    pass


class Common:

    def __init__(self):
        pass

    def _source_url(self):
        return "http://api.fixer.io/"

    def _get_date_string(self, date_obj):
        if date_obj is None:
            return 'latest'
        date_str = date_obj.strftime('%Y-%m-%d')
        return date_str


class CurrencyRates(Common):

    def get_rates(self, base_cur, date_obj=None):
        date_str = self._get_date_string(date_obj)
        payload = {'base': base_cur}
        source_url = self._source_url() + date_str
        response = requests.get(source_url, params=payload)
        if response.status_code == 200:
            rates = response.json().get('rates', {})
            return rates
        raise RatesNotAvailableError("Currency Rates Source Not Ready")

    def get_rate(self, base_cur, dest_cur, date_obj=None):
        date_str = self._get_date_string(date_obj)
        payload = {'base': base_cur, 'symbols': dest_cur}
        source_url = self._source_url() + date_str
        response = requests.get(source_url, params=payload)
        if response.status_code == 200:
            rate = response.json().get('rates', {}).get(dest_cur)
            if not rate:
                raise RatesNotAvailableError("Currency Rate {0} => {1} not available for Date {2}".format(
                    base_cur, dest_cur, date_str))
            return rate
        raise RatesNotAvailableError("Currency Rates Source Not Ready")

    def convert(self, base_cur, dest_cur, amount, date_obj=None):
        date_str = self._get_date_string(date_obj)
        payload = {'base': base_cur, 'symbols': dest_cur}
        source_url = self._source_url() + date_str
        response = requests.get(source_url, params=payload)
        if response.status_code == 200:
            rate = response.json().get('rates', {}).get(dest_cur, None)
            if not rate:
                raise RatesNotAvailableError("Currency {0} => {1} rate not available for Date {2}.".format(
                    source_url, dest_cur, date_str))
            converted_amount = rate * amount
            return converted_amount
        raise RatesNotAvailableError("Currency Rates Source Not Ready")
