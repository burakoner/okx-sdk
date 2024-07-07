import setuptools

with open("README.md", "r",encoding="utf-8") as fh:
    long_description = fh.read()
    
VERSION = '1.5.0'
DESCRIPTION = 'Up-to-date, most-complete, well-organized, well-documented, easy-to-use OKX Exchange Rest and Websocket API SDK for Python'

setuptools.setup(
    name="okx-sdk",
    version=VERSION,
    author="Burak Öner",
    author_email="info@burakoner.com",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/burakoner/okx-sdk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "importlib-metadata",
        "httpx[http2]",
        "keyring",
        "requests",
        "Twisted",
        "pyOpenSSL"
    ],
    keywords=[
        'okx',
        'crypto',
        'exchange',
        'api',
        'sdk',
        'stream',
        'websocket',
        'ws',
        'python',
        'bitcoin',
        'btc',
        'spot',
        'futures',
        'trade'],
)