import requests
import datetime


class RateNotFoundError(Exception):
    """
    Custom exception when conversion rate not found for given Country
    """
    pass


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

    def _validate_date(self, date_str):
        try:
            datetime.datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect date String, date_str should be YYYY-MM-DD")


class CurrencyRates(Common):

    def get_rates(self, base_cur, date_str=None):

        if date_str is None:
            date_str = 'latest'
        else:
            self._validate_date(date_str)
            date_str = str(date_str)

        payload = {'base': base_cur}
        source_url = self._source_url() + date_str
        response = requests.get(source_url, params=payload)
        if response.status_code == 200:
            rates = response.json().get('rates', {})
            return rates
        raise RatesNotAvailableError("Currency Rates Source Not Ready")

    def get_rate(self, base_cur, dest_cur, date_str=None):
        if date_str is None:
            date_str = 'latest'
        else:
            self._validate_date(date_str)
            date_str = str(date_str)

        payload = {'base': base_cur, 'symbols': dest_cur}
        source_url = self._source_url() + date_str
        response = requests.get(source_url, params=payload)
        if response.status_code == 200:
            print response.json()
            rate = response.json().get('rates', {}).get(dest_cur)
            return rate
        raise RatesNotAvailableError("Currency Rates Source Not Ready")

    # def convert(self, base_cur, dest_cur, amount, date_str=None)
