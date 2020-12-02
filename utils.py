import boto3
import requests
from bs4 import BeautifulSoup
import os
import time

def send_text(message):
    
    # Create an SNS client
    client = boto3.client(
        "sns",
        aws_access_key_id=os.environ["AWS_ACCESS_KEY"],
        aws_secret_access_key=os.environ["AWS_SECRET_KEY"],
        region_name='us-east-1'
    )

    number = os.environ['PHONE_NUMBER']
    client.publish(Message=message, PhoneNumber=number) 

def scanner(urls, element, class_name):
    '''
    Scrape urls html response for stock availability and text subscribers if in stock
    params:
    urls: urls we want to scrape
    element: which element we want to scrape for
    class_name: which class name we need to get to differentiate add to cart button
    '''
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
    'Content-Type': 'text/html',
    }

    while True:
        for k, v in urls.items():
            url = v.get('url')
            available = v.get('available')
            try:
                res = requests.get(url, headers=headers)
                html = res.text
                soup = BeautifulSoup(html, 'html.parser')
                status = soup.findAll(element, {"class": class_name})
                if len(status) != 0 and not available:
                    message = f"{k} card in stock! Here is the url: {url}"
                    print(message)
                    send_text(message)
                    urls[k]["available"] = True
                elif len(status) == 0:
                    # once card is out of stock, add to cart button is gone, so flip availability back to false
                    urls[k]["available"] = False
                    print(f"{k} card not in stock!")
            except:
                print("sent too many requests..sleeping")
                time.sleep(30)