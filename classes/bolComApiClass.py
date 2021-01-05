### This is WIP and check more details about the open api  on partnerblog.bol.com

import requests


class bolComApiClass():
    def __init__(self, apiKey):
        self.apiKey = apiKey

    def get_stock_of_product_id(self, productId):
        parameters = {
            "apikey": self.apiKey
        }
        response = requests.get("https://api.bol.com/catalog/v4/products/" + str(productId), params=parameters)
        if response.status_code == 200:
            json_object = response.json()

            if json_object['OfferData']['bol.com'] > 0:
               return json_object['OfferData']['bol.com']

            return 0