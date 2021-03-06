# MMS Portal Extractor

MMS Portal Extractor uses Selenium with PhantomJS to login to the MMS Parent Portal and extract
current grade information for your student. The extracted data can be sent through email to any
specified email addresses.

## Requirements

Install Selenium with Pip and PhantomJS with Brew:

```
pip install selenium
brew install phantomjs
```

## Setup

Clone mms-portal from the command line:

```
https://github.com/melshafer/mms-portal.git
```

Rename `config_sample.py` to `config.py`.

Edit the `config.py` file with the necessary credentials (default/example values are included),
and uncomment those lines.

Edit the `run.sh` file with your path to the `send_email.py` file.


## How to run

From the command line:

```
./mms-portal/run.sh
```

## Email screenshot

![MMS Portal email screenshot](screenshot.png "MMS Portal email screenshot")
