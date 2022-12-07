import os

from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, 'README.md')) as f:
    README = f.read()

setup(
    name='python-serverless',
    long_description=README,
    version='0.0.1',
    install_requires=[],
    packages=["python_serverless"],
    author='Leon Patmore',
    description=''
)
