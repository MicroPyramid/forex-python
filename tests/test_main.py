import unittest
import os
from forex_python.__main__ import run, symbol
try:
    import dbus
except ImportError:
    dbus = False


class TestCLI(unittest.TestCase):
    """Test forex-python command-line interface."""

    def test_defaults(self):
        with open(os.devnull, "w") as null:
            run([], output=null)

    @unittest.skipIf(not dbus, "dbus is not available")
    def test_notify(self):
        run(["--notify"])

    def test_options(self):
        with open(os.devnull, "w") as null:
            run(["-b", "GBP", "-d", "EUR", "-a", "121"], null)

    def test_symbol(self):
        assert symbol("EUR") == u"\u20ac"

if __name__ == "__main__":
    unittest.main()
