from selenium import webdriver
from datetime import datetime

browser = webdriver.Firefox()


def bestBuy(card):
    bestbuy_status = browser.find_element_by_xpath(
        "/html/body/div[1]/div/div[4]/div[1]/div[2]/div[2]/div[4]/div/div[1]/div/p/span").get_attribute("innerHTML")
    print(bestbuy_status)
    now = datetime.now().time()
    if bestbuy_status == "Available to ship":
        return "BUY BUY BUY " + str(now)
    else:
        return "out of stock. " + str(now)


def main():
    card = "3060ti"
    #browser.get("https://www.bestbuy.ca/en-ca/product/nvidia-geforce-rtx-3060-ti-8gb-gddr6-video-card/15166285")
    browser.get("https://www.bestbuy.ca/en-ca/product/amd-ryzen-7-5800x-octa-core-3-8ghz-am4-desktop-processor/15331715")
    while True:
        browser.refresh()
        print(bestBuy(card))

main()
