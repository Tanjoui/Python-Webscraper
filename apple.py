


iphone11 = 'https://www.apple.com/fr/shop/buy-iphone/iphone-11'

import re
import pycurl
from io import BytesIO
b_obj = BytesIO()
crl = pycurl.Curl()
crl.setopt(crl.URL, 'https://www.apple.com/fr/shop/buy-iphone/iphone-11')
crl.setopt(crl.WRITEDATA, b_obj)
crl.perform()
crl.close()
get_body = b_obj.getvalue()
print('Output of GET request:\n%s' % get_body.decode('utf8'))

from datetime import date

today = date.today()
print("Today's date:", today)

price_regex = re.compile(r'("EUR","price"):(\d+)')
pricelist = re.findall(price_regex, get_body.decode('utf8'))


for price in pricelist:
    print(price[1])

min(pricelist)
max(pricelist)

result= {
    "model":"iphone11",
    "date":today,
    "minprice":,
    "maxprice":,
}
