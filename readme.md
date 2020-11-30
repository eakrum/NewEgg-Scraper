## New Egg RTX 3080 in stock notifier.

I made this little script to scan New Egg's website and text me whenever the latest 3080 GPU's come in stock. It leverages AWS to send me text messages, and beautiful soup to quickly parse through raw html for the elements I am looking for to determine stock availability.

I've set up an example `.env` for the variables needed to run this script.

## NOTE:

I am not parsing for all 3080s available, just the ones I am interested in, but theoretically with slight modification this can be used to monitor stock for any product on New Egg's website, i.e 3080, 3090, AMD 5950x, 5900x, 6800 XT etc.

## Prerequisites

Make sure you have an AWS account with CLI credentials. These credentials will supply you with an access key and secret key which we will need to enable the text messaging functionality.

## Installation

I've tested this with python 3.6.9 on an Ubuntu 18.04 on my WSL subsytem. I encourage you to run this script on any linux or mac instance as I have not tested this on Windows.

Clone this repository and run ```pip3 install -r requirements.txt```

This will get all of our dependencies sorted for the script to run.

## Running

We leverage the `python-dotenv` library to automatically source all of our env vars. Our source of truth will be the `.env` file located in this dir. Just simply replace your values for access key, secret key, and phone number with real values.

After completion run `python3 main.py` and wait for stock to be available :). 

## Remarks

There could be many things we can do here to improve this script I just stopped here since I got core functionality done with. I am open to using different tools such as twilio for notifications, I'm just familiar with AWS so I went in that direction. If anybody wants to add onto this or scrape for different sites feel free to open a PR or a new issue and we can colaborate together. This repository can be used to have an open discussion and/or be leveraged as a foundation for a bigger open sourced scraper. I am open to any ideas. 

Here is a little snippet of some example ouput: 
```EVGA_RTX_3080_FTW3 card not in stock!
EVGA_RTX_3080_XC3 card not in stock!
MSI_RTX_3080 card not in stock!
MSI_SUPRIM_RTX_3080 card not in stock!
AORUS_MASTER_RTX_3080 card not in stock!
AORUS_XTREME_RTX_3080 card not in stock!
EAGLE_RTX_3080 card not in stock!
VISION_RTX_3080 card not in stock!
Strix_RTX_3080 card not in stock!
PNY_RTX_3080 card not in stock!
EVGA_RTX_3080_FTW3 card not in stock!
EVGA_RTX_3080_XC3 card not in stock!
MSI_RTX_3080 card not in stock!
MSI_SUPRIM_RTX_3080 card not in stock!