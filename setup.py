from setuptools import setup

try:
    long_description = open('README').read()
except:
    long_description = ''

setup(
    name = 'efzp',
    version = '1.1',
    description = 'Describe an email in terms of salutation, body, signature, reply text etc.',
    author = 'Dave Trindall',
    url = 'https://github.com/Trindaz/EFZP',
    packages = ['efzp'],
    license = 'Apache License 2.0',
)

