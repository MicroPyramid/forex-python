from unittest import TestCase
from forex_python.converter import CurrencyRates


class TestBase(TestCase):
    def setUp(self):
        c = CurrencyRates()


class TestGetRates(TestBase):
    """
    Test get_rates with valid(ex: USD) and invalid(ex: XYZ) currency code
    """
    def test_get_rates_valid_code(self):
        all_rates = c.get_rates('USD')

        # Check if return value of get_rates dictionary
        self.assertTrue(isinstance(all_rates, dict))

        # Test at least one rate value returned
        self.assertTrue(len(all_rates.keys()))

        # Test one rate in returned dict is float value
        self.assertTrue(isinstance(all_rates.get('INR'), float))

    def test_get_rates_invalid_code(self):
        all_rates = c.get_rates('XYZ')

        # Check if return value of get_rates dictionary
        self.assertTrue(isinstance(all_rates, dict))

        # Test no values in dict(empty dict)
        self.assertFalse(len(all_rates.keys()))

        # Test one rate in returned dict is not float value
        self.assertFalse(isinstance(all_rates.get('INR'), float))


class TestGetRate(TestBase):
    """
    Test get_rate function using valid and invalid currency codes
    """

    def test_get_rate_with_valid_codes(self):
        rate = c.get_rate(self, 'USD', 'INR')

        # check if return value is float
        self.assertTrue(isinstance(rate, float))

    def test_get_rate_with_invalid_codes(self):
        # raise exception for invalid currency codes
        self.assertRaises(RatesNotAvailableError, c.get_rate(self, 'ABCD', 'XYZ'))


class TestAmountConvert(TestBase):
    """
    test amount conversion from one currency to other
    """

    def test_amount_convert_valid_currency(self):
        amount = c.convert('USD', 'INR', 10)

        # test if amount returned in float
        self.assertTrue(isinstance(amount, float))

    def test_amount_convert_valid_currency(self):
        # test if amount returned in float
        self.assertRaises(RateNotFoundError, c.convert('ABC, 'XYZ', 10))
