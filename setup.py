import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='netsuite_sdk_py',
    version = '1.0.2',
    package_dir={"netsuitesdk": "netsuitesdk"},
    packages = ['netsuitesdk'],
    author = 'Precanto',
    license="MIT",
    author_email = 'sagar@precanto.com',
    description = 'Python SDK for accessing the NetSuite SOAP webservice',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url = 'https://github.com/Precanto/py-netsuite-sdk',
    download_url = 'https://github.com/Precanto/py-netsuite-sdk/archive/refs/tags/1.0.1.tar.gz',
    keywords=['netsuite', 'api', 'python', 'sdk'],
    install_requires=["zeep", "requests"],
    include_package_data=True,
    python_requires=">=3.6",
    classifiers = [
        'Topic :: Internet :: WWW/HTTP',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ]
)