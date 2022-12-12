import os

from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, 'README.md')) as f:
    README = f.read()

setup(
    name='python-serverless',
    long_description=README,
    version='0.0.5',
    install_requires=[],
    packages=find_packages(exclude=["tests"]),
    author='Leon Patmore',
    description=''
)
