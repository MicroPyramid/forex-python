import requests
import datetime


class RateNotFoundError(Exception):
    """
    Custom exception when conversion rate not found for given Country
    """
    pass


class SourceNotReadyError(Exception):
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

    def get_all_rates(self, base_cur, date_str=None):

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
            print type(rates)
            return rates
        raise SourceNotReadyError("Currency Rates Source Not Ready")
