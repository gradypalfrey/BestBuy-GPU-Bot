import time

from selenium import webdriver
from datetime import datetime

from twilio.rest import Client

browser = webdriver.Firefox(executable_path=r'C:/Users/grady/Downloads/geckodriver-v0.29.0-win64/geckodriver')

# Twilio
number = "+16043121279"
fromNumber = "+17034680663"
accountSID = "AC49c954e929d3f6541a0b255098c11f39"
authToken = "9af27e4e206e9abf1a6e3e47f90d44d3"
client = Client(accountSID, authToken)


def bestBuy(card, n):
    bestbuy_status = browser.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[1]/div[2]/div[2]/div[4]/div/div[1]/div/p/span").get_attribute("innerHTML")
    now = datetime.now().time()
    if bestbuy_status == "Available to ship":
        client.messages.create(to=number, from_=fromNumber, body="Buy a 3060-ti!")
        return str(n) + ". BUY BUY BUY " + card + " " + str(now)
    else:
        return str(n) + ". out of stock. " + str(now)


def main():
    card = "3060ti"
    browser.get("https://www.bestbuy.ca/en-ca/product/nvidia-geforce-rtx-3060-ti-8gb-gddr6-video-card/15166285")
    # browser.get("https://www.bestbuy.ca/en-ca/product/amd-ryzen-7-5800x-octa-core-3-8ghz-am4-desktop-processor/15331715")
    n = 1
    while True:
        browser.refresh()
        print(bestBuy(card, n))
        time.sleep(5)
        n += 1

main()
