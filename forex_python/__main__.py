"""Command line utilty for forex-python
=======================================

Inspired by another package: anshulc95/exch
"""
import argparse
import os

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


def conversion_result(amount, base, converted_amount, dest):
    return "{} {} = {} {}".format(amount, base, converted_amount, dest)


def notify_posix(args):
    try:
        import notify2
    except ImportError:
        print("Requires Linux or macOS with notify2 and dbus package.")
        raise
    notify2.init("forex-python")
    notification = conversion_result(
        1.0, args.base, converter.get_rate(args.base, args.dest), args.dest
    )
    n = notify2.Notification(
        "forex-python", notification, "notification-message-im"  # Icon name
    )
    n.show()


def run():
    args = parser.parse_args()
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
            )
        )
