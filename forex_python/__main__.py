"""Command line utilty for forex-python
=======================================

Inspired by another package: anshulc95/exch
"""
from __future__ import print_function

import argparse
import os
import sys

from . import converter


parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
parser.add_argument(
    "-b", "--base", default="USD", help="Currency you are converting from."
)
parser.add_argument(
    "-d", "--dest", default="INR", help="Currency you are converting to."
)
parser.add_argument(
    "-a", "--amount", default=1.0, type=float, help="Amount to convert."
)
parser.add_argument(
    "-n", "--notify", action="store_true", help="Display desktop alerts."
)


def symbol(currency_code):
    sym = converter.get_symbol(currency_code)
    if sym is not None:
        return sym
    else:
        return currency_code


def conversion_result(amount, base, converted_amount, dest, use_symbols=False):
    if use_symbols:
        return "{} {} = {} {}".format(
            symbol(base), amount, symbol(dest), converted_amount
        )
    else:
        return "{} {} = {} {}".format(amount, base, converted_amount, dest)



def notify_posix(args):
    try:
        import notify2
    except ImportError:
        print("Requires Linux or macOS with notify2 and dbus package.")
        raise
    notify2.init("forex-python")
    notification = conversion_result(
        1.0, args.base, converter.get_rate(args.base, args.dest), args.dest,
        True
    )
    n = notify2.Notification(
        "forex-python", notification, "notification-message-im"  # Icon name
    )
    n.show()


def run(args=None, output=sys.stdout):
    args = parser.parse_args(args)
    if args.notify:
        if os.name == "posix":
            notify_posix(args)
    else:
        print(
            conversion_result(
                args.amount,
                args.base,
                converter.convert(args.base, args.dest, args.amount),
                args.dest,
            ),
            file=output
        )
