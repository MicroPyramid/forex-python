import requests


class BtcConverter(object):
    """
    Get bit coin rates convert
    """

    def get_latest_price(self, currency):
        url = 'https://api.coindesk.com/v1/bpi/currentprice/{}.json'.format(currency)
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            price = data.get('bpi').get(currency, {}).get('rate_float', None)
            return price
        return None

    def get_previous_price(self, currency, date_obj):
        start = date_obj.strftime('%Y-%m-%d')
        end = date_obj.strftime('%Y-%m-%d')
        url = (
            'https://api.coindesk.com/v1/bpi/historical/close.json'
            '?start={}&end={}&currency={}'.format(
                   start, end, currency
               )
        )
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            price = data.get('bpi', {}).get(start, None)
            return price
        return None

    def get_previous_price_list(self, currency, start_date, end_date):
        start = start_date.strftime('%Y-%m-%d')
        end = end_date.strftime('%Y-%m-%d')
        url = (
            'https://api.coindesk.com/v1/bpi/historical/close.json'
            '?start={}&end={}&currency={}'.format(
                   start, end, currency
               )
        )
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            price_dict = data.get('bpi', {})
            return price_dict
        return {}

    def convert_to_btc(self, amount, currency):
        url = 'https://api.coindesk.com/v1/bpi/currentprice/{}.json'.format(currency)
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            price = data.get('bpi').get(currency, {}).get('rate_float', None)
            if price:
                converted_btc = amount/price
                return converted_btc
            return None
        return None

    def convert_btc_to_cur(self, coins, currency):
        url = 'https://api.coindesk.com/v1/bpi/currentprice/{}.json'.format(currency)
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            price = data.get('bpi').get(currency, {}).get('rate_float', None)
            if price:
                converted_amount = coins * price
                return converted_amount
            return None
        return None

    def convert_to_btc_on(self, amount, currency, date_obj):
        start = date_obj.strftime('%Y-%m-%d')
        end = date_obj.strftime('%Y-%m-%d')
        url = (
            'https://api.coindesk.com/v1/bpi/historical/close.json'
            '?start={}&end={}&currency={}'.format(
                   start, end, currency
               )
        )
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            price = data.get('bpi', {}).get(start, None)
            if price:
                converted_btc = amount/price
                return converted_btc
            return None
        return None

    def convert_btc_to_cur_on(self, coins, currency, date_obj):
        start = date_obj.strftime('%Y-%m-%d')
        end = date_obj.strftime('%Y-%m-%d')
        url = (
            'https://api.coindesk.com/v1/bpi/historical/close.json'
            '?start={}&end={}&currency={}'.format(
                   start, end, currency
               )
        )
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            price = data.get('bpi', {}).get(start, None)
            if price:
                converted_btc = coins*price
                return converted_btc
            return None
        return None

    def get_symbol(self):
        return "\u0E3F"
