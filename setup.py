import io
import os
from setuptools import setup, find_packages

VERSION = '0.3.2'

setup(
    name='forex-python',
    version=VERSION,
    author='Micro Pyramid Informatic Pvt. Ltd.',
    author_email='hello@micropyramid.com',
    url='https://github.com/MicroPyramid/forex-python',
    description='Foreign exchange rates and currency conversion.',
    long_description="\n\n".join([open("README.rst").read()]),
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    install_requires=[
        'requests',
        'simplejson',
    ],
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
)
