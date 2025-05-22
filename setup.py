import io
import os
from setuptools import setup, find_packages

# 1) Bump this version each release:
VERSION = '1.9.2'

# 2) Pull your README.md in as long_description:
here = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='forex-python',
    version=VERSION,
    author='Micro Pyramid Informatic Pvt. Ltd.',
    author_email='hello@micropyramid.com',
    description='Free foreign exchange rates and currency conversion.',
    long_description=long_description,
    long_description_content_type='text/markdown',  # so PyPI renders your README properly
    url='https://github.com/MicroPyramid/forex-python',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    install_requires=[
        'requests>=2.0',
        'simplejson>=3.0',
    ],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, <4',
    classifiers=[
        # audience
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Internationalization',
        # license
        'License :: OSI Approved :: MIT License',
        # OS
        'Operating System :: OS Independent',
        # languages
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    project_urls={   # these show up as “Project Links” on PyPI
        'Documentation': 'https://forex-python.readthedocs.io/',
        'Source': 'https://github.com/MicroPyramid/forex-python',
        'Tracker': 'https://github.com/MicroPyramid/forex-python/issues',
    },
)
