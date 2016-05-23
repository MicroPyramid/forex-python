from setuptools import setup, find_packages

VERSION = 0.1

with open('README.md') as fl:
    LONG_DESCRIPTION = fl.read()

with open('LICENSE') as fl:
    LICENSE = fl.read()

setup(
    name='forex-python',
    version=VERSION,
    author='Micro Pyramid Informatic Pvt. Ltd.',
    author_email='hello@micropyramid.com',
    url='https://github.com/MicroPyramid/forex-python',
    description='Foreign exchange rates and currency conversion.',
    long_description=LONG_DESCRIPTION,
    license=LICENSE,
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    install_requires=[
        'requests',
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
