import datetime
from unittest import TestCase
from forex_python.bitcoin import BtcConverter


class TestCommon(TestCase):
    """
    Common class with setUp method for all test cases
    """
    def setUp(self):
        self.b = BtcConverter()

    
class TestLatestPrice(TestCommon):
    """
    Test get latest price using currency code
    """
    def test_latest_price_valid_currency(self):
        price = self.b.get_latest_price('USD')
        self.assertEqual(type(price), float)

    def test_latest_price_invalid_currency(self):
        price = self.b.get_latest_price('XYZ')
        self.assertFalse(price)


class TestPreviousPrice(TestCommon):
    """
    Test Price with date input
    """
    def test_previous_price_valid_currency(self):
        date_obj = datetime.datetime.today() - datetime.timedelta(days=15)
        price = self.b.get_previous_price('USD', date_obj)
        self.assertEqual(type(price), float)

    def test_previous_price_invalid_currency(self):
        date_obj = datetime.datetime.today() - datetime.timedelta(days=15)
        price = self.b.get_previous_price('XYZ', date_obj)
        self.assertFalse(price)


class TestPreviousPriceList(TestCommon):
    """
    Test previous price list for a currency
    """
    def test_previous_price_list_with_valid_currency(self):
        start_date = datetime.datetime.today() - datetime.timedelta(days=15)
        end_date = datetime.datetime.today()
        price_list = self.b.get_previous_price_list('USD', start_date, end_date)
        self.assertTrue(price_list)
        self.assertEqual(type(price_list), dict)

    def test_previous_price_list_with_invalid_currency(self):
        start_date = datetime.datetime.today() - datetime.timedelta(days=15)
        end_date = datetime.datetime.today()
        price_list = self.b.get_previous_price_list('XYZ', start_date, end_date)
        self.assertFalse(price_list)
        self.assertEqual(type(price_list), dict)


class TestConvertBtc(TestCommon):
    """
    Test Converting amount to Bit coins
    """
    def test_convet_to_btc_with_valid_currency(self):
        coins = self.b.convert_to_btc(250, 'USD')
        self.assertEqual(type(coins), float)

    def test_convet_to_btc_with_invalid_currency(self):
        coins = self.b.convert_to_btc(250, 'XYZ')
        self.assertFalse(coins)


class TestConvertBtcToCur(TestCommon):
    """
    Convert Bit Coins to Valid Currency amount
    """
    def test_convert_btc_to_cur_valid_currency(self):
        amount = self.b.convert_btc_to_cur(2, 'USD')
        self.assertEqual(type(amount), float)

    def test_convert_btc_to_cur_invalid_currency(self):
        amount = self.b.convert_btc_to_cur(2, 'XYZ')
        self.assertFalse(amount)


class TestConvertToBtcOn(TestCommon):
    """
    Convert To bit coin based on previous dates
    """
    def test_convert_to_btc_on_with_valid_currency(self):
        date_obj = datetime.datetime.today() - datetime.timedelta(days=15)
        coins = self.b.convert_to_btc_on(300, 'USD', date_obj)
        self.assertEqual(type(coins), float)

    def test_convert_to_btc_on_with_invalid_currency(self):
        date_obj = datetime.datetime.today() - datetime.timedelta(days=15)
        coins = self.b.convert_to_btc_on(300, 'XYZ', date_obj)
        self.assertFalse(coins)


class TestConvertBtcToCurOn(TestCommon):
    """
    Convert BitCoins to valid Currency
    """
    def test_convert_to_btc_on_with_valid_currency(self):
        date_obj = datetime.datetime.today() - datetime.timedelta(days=15)
        amount = self.b.convert_btc_to_cur_on(3, 'USD', date_obj)
        self.assertEqual(type(amount), float)

    def test_convert_to_btc_on_with_invalid_currency(self):
        date_obj = datetime.datetime.today() - datetime.timedelta(days=15)
        amount = self.b.convert_btc_to_cur_on(3, 'XYZ', date_obj)
        self.assertFalse(amount)


class TestBitCoinSymbol(TestCommon):
    """
    Bit Coin symbol
    """
    def test_bitcoin_symbol(self):
        self.assertEqual(self.b.get_symbol(), "\u0E3F")
