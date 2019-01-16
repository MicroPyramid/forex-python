import os
from setuptools import setup, find_packages

VERSION = '1.0.0'
long_description_text = """Forex Python is a Free Foreign exchange rates and currency conversion.
Features:
List all currency rates.
BitCoin price for all curuncies.
Converting amount to BitCoins.
Get historical rates for any day since 1999.
Conversion rate for one currency(ex; USD to INR).
Convert amount from one currency to other.('USD 10$' to INR).
Currency symbols.
Currency names.

Documentation: http://forex-python.readthedocs.io/en/latest/usage.html
GitHub: https://github.com/MicroPyramid/forex-python

"""

install_requires=[
    'requests',
    'simplejson',
]

if os.name == 'posix':
    install_requires += [
        'notify2',
        'dbus-python'
    ]

setup(
    name='forex-python',
    version=VERSION,
    author='Micro Pyramid Informatic Pvt. Ltd.',
    author_email='hello@micropyramid.com',
    url='https://github.com/MicroPyramid/forex-python',
    description='Foreign exchange rates and currency conversion.',
    long_description=long_description_text,
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    install_requires=install_requires,
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Internationalization',
    ],
    entry_points={
        'console_scripts':
        ['forex-python=forex_python.__main__:run']
    },
)
