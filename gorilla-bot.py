# imports
import requests as req
import json
import os
import time
from twilio.rest import Client
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

def sendMessage(message, fromNumber, toNumber, client):
    message = client.messages \
                .create(
                     body=message,
                     from_=fromNumber,
                     to=toNumber
                 )
    print(message.sid)

def checkSiteJson(productsToCheck):
    SHOP_URL = 'https://gorillamind.com'
    request = req.get(f'{SHOP_URL}/products.json')
    availableProducts = []
    if request.status_code == 200:
        data = request.json()
        products = data['products']
        for product in products:
            title = product.get('title')
            if (title in productsToCheck):
                variants = product.get('variants')
                for variant in variants:
                    isAvailable = variant.get('available')
                    if isAvailable:
                        availableProducts.append(title)

    return availableProducts


# gets configuration data from './config.json' file
def getCongigData():
    with open ('./config.json', 'r') as file:
        return json.load(file)

# check site pages for products in stock
def checkPages(targetPages):
    # only parse for script tags, increase performance
    onlyScriptTags = SoupStrainer("script")
    availableProducts = []
    for page in targetPages:
        r = req.get(page)
        if r.status_code == 200:
            htmlContent = r.text
            soup = BeautifulSoup(htmlContent, 'html.parser', parse_only=onlyScriptTags)
            productScriptTags = soup.find_all('script', id="tfx-product")
            for scriptTag in productScriptTags:
                tagContents = scriptTag.contents[0]
                jsonStartIndex = tagContents.index("{")
                jsonEndIndex = tagContents.rindex("}") + 1
                jsonBlob = tagContents[jsonStartIndex:jsonEndIndex]
                jsonBlobData = json.loads(jsonBlob)
                title = jsonBlobData.get('title')
                isAvailable = jsonBlobData.get('available')
                if isAvailable == True:
                    availableProducts.append(title)           
    return availableProducts

if __name__ == '__main__':
    # config data
    configData = getCongigData()
    targetProductPages = configData.get('targetProductPages')
    targetProducts = configData.get('targetProducts')
    targetPhones = configData.get('targetPhones')
    # twilio variables
    accountSid = os.environ['TWILIO_ACCOUNT_SID']
    authToken = os.environ['TWILIO_AUTH_TOKEN']
    fromNumber = os.environ['TWILIO_NUMBER']
    client = Client(accountSid, authToken)
    # check time in seconds -> 5 minutes
    checkTime = 300.0
    for phoneNum in targetPhones:
        sendMessage("Gorilla Bot is Active", fromNumber, phoneNum, client)
    print("bot successfully deployed")
    while True:
        time.sleep(checkTime - time.time() % checkTime)
        availableProductsFromPages = checkPages(targetProductPages)
        availableProductsFromSiteJson = checkSiteJson(targetProducts)
        if (len(availableProductsFromPages) > 0):
            for product in availableProductsFromPages:
                for toNumber in targetPhones:
                    sendMessage(product + "is in stock", fromNumber, toNumber, client)
        if (len(availableProductsFromSiteJson) > 0):
            for product in availableProductsFromSiteJson:
                for toNumber in targetPhones:
                    sendMessage(product + "is in stock", fromNumber, toNumber, client)