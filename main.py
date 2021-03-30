import time

from selenium import webdriver
from datetime import datetime

from twilio.rest import Client

import random

browser = webdriver.Firefox(executable_path=r'C:/Users/grady/Downloads/geckodriver-v0.29.0-win64/geckodriver')

# Twilio
number = ""
fromNumber = ""
accountSID = ""
authToken = ""
client = Client(accountSID, authToken)


class Card:
    def __init__(self, name, link, status):
        self.name = name
        self.link = link
        self.status = status

    def best_buy(self, n):
        time.sleep(random.randint(3, 6))
        bestbuy_status = browser.find_element_by_xpath(
            "/html/body/div[1]/div/div[4]/div[1]/div[2]/div[2]/div[4]/div/div[1]/div/p/span").get_attribute("innerHTML")
        now = datetime.now().time()
        if bestbuy_status == "Available to ship":
            self.status = True
            client.messages.create(to=number, from_=fromNumber, body="Buy a " + self.name + " at " + self.link)
            return str(n) + "\t\tBuy a " + self.name + " at " + self.link + "\t\t" + str(now)
        else:
            return str(n) + "\t\t" + self.name + ":\t" + bestbuy_status + "\t\t" + str(now)


def main():

    nvidia = Card("Nvidia", "https://www.bestbuy.ca/en-ca/product/nvidia-geforce-rtx-3060-ti-8gb-gddr6-video-card/15166285", False)
    evga = Card("Evga", "https://www.bestbuy.ca/en-ca/product/evga-nvidia-geforce-rtx-3060-ti-ftw3-ultra-8gb-gddr6-video-card/15229237", False)
    msi = Card("MSI", "https://www.bestbuy.ca/en-ca/product/msi-nvidia-geforce-rtx-3060-ti-ventus-2x-oc-8gb-gddr6-video-card/15178453", False)
    # zotac = Card("Zotac", "https://www.bestbuy.ca/en-ca/product/zotac-geforce-rtx-3060-ti-twin-edge-oc-8gb-gddr6-video-card/15178452", False)
    tuff = Card("Tuff", "https://www.bestbuy.ca/en-ca/product/asus-tuf-gaming-geforce-rtx-3060-ti-oc-8gb-gddr6-video-card/15201200", False)

    n = 1
    while True:
        browser.get(nvidia.link)
        print(nvidia.best_buy(n))

        browser.get(evga.link)
        print(evga.best_buy(n))

        browser.get(msi.link)
        print(msi.best_buy(n))

        # browser.get(zotac.link)
        # print(zotac.best_buy(n))

        browser.get(tuff.link)
        print(tuff.best_buy(n))

        n += 1


main()
