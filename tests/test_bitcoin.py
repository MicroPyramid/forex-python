import datetime
from decimal import Decimal
from unittest import TestCase
from forex_python.bitcoin import (get_btc_symbol, convert_btc_to_cur_on, convert_to_btc_on,
                            convert_btc_to_cur, convert_to_btc, get_latest_price,
                            get_previous_price, get_previous_price_list, BtcConverter)
from forex_python.converter import RatesNotAvailableError, DecimalFloatMismatchError


class TestLatestPrice(TestCase):
    """
    Test get latest price using currency code
    """
    def test_latest_price_valid_currency(self):
        price = get_latest_price('USD')
        self.assertEqual(type(price), float)

    def test_latest_price_invalid_currency(self):
        price = get_latest_price('XYZ')
        self.assertFalse(price)


class TestPreviousPrice(TestCase):
    """
    Test Price with date input
    """
    def test_previous_price_valid_currency(self):
        date_obj = datetime.datetime.today() - datetime.timedelta(days=15)
        price = get_previous_price('USD', date_obj)
        self.assertEqual(type(price), float)

    def test_previous_price_invalid_currency(self):
        date_obj = datetime.datetime.today() - datetime.timedelta(days=15)
        self.assertRaises(RatesNotAvailableError, get_previous_price, 'XYZ', date_obj)


class TestPreviousPriceList(TestCase):
    """
    Test previous price list for a currency
    """
    def test_previous_price_list_with_valid_currency(self):
        start_date = datetime.datetime.today() - datetime.timedelta(days=15)
        end_date = datetime.datetime.today()
        price_list = get_previous_price_list('USD', start_date, end_date)
        self.assertTrue(price_list)
        self.assertEqual(type(price_list), dict)

    def test_previous_price_list_with_invalid_currency(self):
        start_date = datetime.datetime.today() - datetime.timedelta(days=15)
        end_date = datetime.datetime.today()
        price_list = get_previous_price_list('XYZ', start_date, end_date)
        self.assertFalse(price_list)
        self.assertEqual(type(price_list), dict)


class TestConvertBtc(TestCase):
    """
    Test converting amount to Bitcoin
    """
    def test_convet_to_btc_with_valid_currency(self):
        coins = convert_to_btc(250, 'USD')
        self.assertEqual(type(coins), float)

    def test_convet_to_btc_with_invalid_currency(self):
        self.assertRaises(RatesNotAvailableError, convert_to_btc, 250, 'XYZ')


class TestConvertBtcToCur(TestCase):
    """
    Convert Bitcoin to valid currency amount
    """
    def test_convert_btc_to_cur_valid_currency(self):
        amount = convert_btc_to_cur(2, 'USD')
        self.assertEqual(type(amount), float)

    def test_convert_btc_to_cur_invalid_currency(self):
        self.assertRaises(RatesNotAvailableError, convert_btc_to_cur, 2, 'XYZ')


class TestConvertToBtcOn(TestCase):
    """
    Convert to Bitcoin based on previous date
    """
    def test_convert_to_btc_on_with_valid_currency(self):
        date_obj = datetime.datetime.today() - datetime.timedelta(days=15)
        coins = convert_to_btc_on(300, 'USD', date_obj)
        self.assertEqual(type(coins), float)

    def test_convert_to_btc_on_with_invalid_currency(self):
        date_obj = datetime.datetime.today() - datetime.timedelta(days=15)
        self.assertRaises(RatesNotAvailableError, convert_to_btc_on, 300, 'XYZ', date_obj)


class TestConvertBtcToCurOn(TestCase):
    """
    Convert Bitcoin to valid currency
    """
    def test_convert_to_btc_on_with_valid_currency(self):
        date_obj = datetime.datetime.today() - datetime.timedelta(days=15)
        amount = convert_btc_to_cur_on(3, 'USD', date_obj)
        self.assertEqual(type(amount), float)

    def test_convert_to_btc_on_with_invalid_currency(self):
        date_obj = datetime.datetime.today() - datetime.timedelta(days=15)
        self.assertRaises(RatesNotAvailableError, convert_btc_to_cur_on, 3, 'XYZ', date_obj)


class TestBitCoinSymbol(TestCase):
    """
    Bitcoin symbol
    """
    def test_bitcoin_symbol(self):
        self.assertEqual(get_btc_symbol(), "\u0E3F")


class TestBitCoinWithoutForceDecimal(TestCase):

    def setUp(self):
        self.b = BtcConverter()

    def test_latest_price_valid_currency(self):
        price = self.b.get_latest_price('USD')
        self.assertEqual(type(price), float)

    def test_latest_price_invalid_currency(self):
        price = self.b.get_latest_price('XYZ')
        self.assertFalse(price)

    def test_previous_price_valid_currency(self):
        date_obj = datetime.datetime.today() - datetime.timedelta(days=15)
        price = self.b.get_previous_price('USD', date_obj)
        self.assertEqual(type(price), float)

    def test_previous_price_invalid_currency(self):
        date_obj = datetime.datetime.today() - datetime.timedelta(days=15)
        self.assertRaises(RatesNotAvailableError, self.b.get_previous_price, 'XYZ', date_obj)

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

    def test_convet_to_btc_with_valid_currency(self):
        coins = self.b.convert_to_btc(250, 'USD')
        self.assertEqual(type(coins), float)

    def test_convet_to_btc_with_invalid_currency(self):
        self.assertRaises(RatesNotAvailableError, self.b.convert_to_btc, 250, 'XYZ')

    def test_convert_btc_to_cur_valid_currency(self):
        amount = self.b.convert_btc_to_cur(2, 'USD')
        self.assertEqual(type(amount), float)

    def test_convert_btc_to_cur_invalid_currency(self):
        self.assertRaises(RatesNotAvailableError, self.b.convert_btc_to_cur, 2, 'XYZ')

    def test_convert_to_btc_on_with_valid_currency(self):
        date_obj = datetime.datetime.today() - datetime.timedelta(days=15)
        coins = self.b.convert_to_btc_on(300, 'USD', date_obj)
        self.assertEqual(type(coins), float)

    def test_convert_to_btc_on_with_invalid_currency(self):
        date_obj = datetime.datetime.today() - datetime.timedelta(days=15)
        self.assertRaises(RatesNotAvailableError, self.b.convert_to_btc_on, 300, 'XYZ', date_obj)

    def test_convert_to_btc_on_with_valid_currency(self):
        date_obj = datetime.datetime.today() - datetime.timedelta(days=15)
        amount = self.b.convert_btc_to_cur_on(3, 'USD', date_obj)
        self.assertEqual(type(amount), float)

    def test_convert_to_btc_on_with_invalid_currency(self):
        date_obj = datetime.datetime.today() - datetime.timedelta(days=15)
        self.assertRaises(RatesNotAvailableError, self.b.convert_btc_to_cur_on, 3, 'XYZ', date_obj)


class TestBitCoinForceDecimal(TestCase):

    def setUp(self):
        self.b = BtcConverter(force_decimal=True)

    def test_latest_price_valid_currency(self):
        price = self.b.get_latest_price('USD')
        self.assertEqual(type(price), Decimal)

    def test_latest_price_invalid_currency(self):
        price = self.b.get_latest_price('XYZ')
        self.assertFalse(price)

    def test_previous_price_valid_currency(self):
        date_obj = datetime.datetime.today() - datetime.timedelta(days=15)
        price = self.b.get_previous_price('USD', date_obj)
        self.assertEqual(type(price), Decimal)

    def test_previous_price_invalid_currency(self):
        date_obj = datetime.datetime.today() - datetime.timedelta(days=15)
        self.assertRaises(RatesNotAvailableError, self.b.get_previous_price, 'XYZ', date_obj)

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

    def test_convert_to_btc_with_valid_currency(self):
        coins = self.b.convert_to_btc(Decimal('250'), 'USD')
        self.assertEqual(type(coins), Decimal)

    def test_convert_to_btc_with_invalid_currency(self):
        self.assertRaises(RatesNotAvailableError, self.b.convert_to_btc, Decimal('250'), 'XYZ')

    def test_convert_btc_to_cur_valid_currency(self):
        amount = self.b.convert_btc_to_cur(Decimal('2'), 'USD')
        self.assertEqual(type(amount), Decimal)

    def test_convert_btc_to_cur_invalid_currency(self):
        self.assertRaises(RatesNotAvailableError, self.b.convert_btc_to_cur, Decimal('250'), 'XYZ')

    def test_convert_to_btc_on_with_valid_currency(self):
        date_obj = datetime.datetime.today() - datetime.timedelta(days=15)
        coins = self.b.convert_to_btc_on(Decimal('300'), 'USD', date_obj)
        self.assertEqual(type(coins), Decimal)

    def test_convert_to_btc_on_with_invalid_currency(self):
        date_obj = datetime.datetime.today() - datetime.timedelta(days=15)
        self.assertRaises(RatesNotAvailableError, self.b.convert_to_btc_on, Decimal('250'), 'XYZ', date_obj)

    def test_convert_to_btc_on_with_valid_currency(self):
        date_obj = datetime.datetime.today() - datetime.timedelta(days=15)
        amount = self.b.convert_btc_to_cur_on(Decimal('250'), 'USD', date_obj)
        self.assertEqual(type(amount), Decimal)

    def test_convert_to_btc_on_with_invalid_currency(self):
        date_obj = datetime.datetime.today() - datetime.timedelta(days=15)
        self.assertRaises(RatesNotAvailableError, self.b.convert_btc_to_cur_on, Decimal('3'), 'XYZ', date_obj)

