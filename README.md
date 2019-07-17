# Parser of phone numbers from web-pages

This script parses phone numbers from web-pages.


## Dependencies:
[python-phonenumbers](https://github.com/daviddrysdale/python-phonenumbers)

## Deployment:
If python 3.7+ is installed on local machine:
    1. Create virtual environment and install 
    requirements with 
    `python3.7 -m virtualenv venv && venv/bin/pip install -r requirements.txt`
    2. Run with 
    `venv/bin/python main.py`
    
With docker:

`docker build -t=phone_parser . && docker run phone_parser`
