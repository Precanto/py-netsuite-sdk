from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='netsuite-sdk-py',
    version = '0.0.8',
    package_dir={"netsuitesdk": "netsuitesdk", "netsuitesdk.api": "netsuitesdk.api"},
    packages = ['netsuitesdk', "netsuitesdk.api"],
    author = 'Precanto',
    license="MIT",
    author_email = 'sagar@precanto.com',
    description = 'Python SDK for accessing the NetSuite SOAP webservice',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url = 'https://github.com/Precanto/py-netsuite-sdk',
    keywords=['netsuite', 'api', 'python', 'sdk'],
    python_requires=">=3.6",
    classifiers = [
        'Topic :: Internet :: WWW/HTTP',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ]
)