import requests
from bs4 import BeautifulSoup
import smtplib


EMAIL = 'xxxx@gmail.com'
EMAIL_PASSWORD = 'xxxx'
TO_EMAIL = 'xxxx@gmail.com'

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; \
                         x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
           'Accept-Language': 'en-US,en;q=0.9'}
WEBSITE = 'https://www.euro.com.pl/pojazdy-elektryczne/acer-hulajnoga-elektr-acer-es-series-3.bhtml'

response = requests.get(url=WEBSITE, headers=HEADERS)
TEXT_WEBSITE = response.text

soup = BeautifulSoup(TEXT_WEBSITE, 'html.parser')

product_headline = soup.find('h1').getText()

div_that_contains_price = soup.find('div', class_="eds-tabs__wrapper")
price = div_that_contains_price.find('span', class_='price-template__x-large--total').getText()

message = f"Subject:{product_headline}\n\n Your product price has dropped down. Now it's {price} pln."

if price < '999':
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=EMAIL_PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=TO_EMAIL, msg=message)
