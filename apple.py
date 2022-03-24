import re
import pycurl
from io import BytesIO
import pandas as pd
from datetime import datetime
import requests
from bs4 import BeautifulSoup


class AppleExtractor():
    model_list = ['iphone-11', 'iphone-12', 'iphone-13', 'iphone-13-pro', 'iphone-se']
    result_list = []

    def find_model(self):
        url = 'https://www.apple.com/fr/shop/buy-iphone/'
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        urls = []
        for link in soup.find_all('a'):
            print(link.get('href'))

    def run(self):
        for model in self.model_list:
            m = ModelExtractor(model)
            row = m.get_page()
            self.result_list.append(row)

    def save_results(self):
        result = pd.DataFrame(self.result_list)
        result.to_csv('AppleModels.csv', mode='a', header=False)


class ModelExtractor:
    def __init__(self, model):
        self.model = model
        self.date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print("Extraction date for ", model, " : ", self.date)

    def get_page(self):
        b_obj = BytesIO()
        crl = pycurl.Curl()
        crl.setopt(crl.URL, 'https://www.apple.com/fr/shop/buy-iphone/' + self.model)
        crl.setopt(crl.WRITEDATA, b_obj)
        crl.perform()
        crl.close()
        get_body = b_obj.getvalue()

        price_regex = re.compile(r'("EUR","price"):(\d+)')
        price_list = []
        for match in price_regex.finditer(get_body.decode('utf8')):
            price_list.append(match.group(2))


        result = {'model': self.model, 'date': self.date, 'min_price': min(price_list), 'max_price': max(price_list),
                  }
        print(result)

        return result


e = AppleExtractor()
e.find_model()
e.run()
e.save_results()
