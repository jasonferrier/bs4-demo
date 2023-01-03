from bs4 import BeautifulSoup

import requests

BASE_URL = "https://www.libib.com/u/ghoover"
# page = requests.get(URL)

# This API endpoint returns a JSON response
GET_ITEMS = BASE_URL + "/get-account-items"
form_data = {'library_id': 77535, 'offset': 0}

data = requests.post(GET_ITEMS, data=form_data)

if data:
    print('Success!')
    print(data.content)
else:
    print('Not Found.')