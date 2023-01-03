from bs4 import BeautifulSoup

import requests
import json

# GeorgeHooverArchitect Collection
BASE_URL = "https://www.libib.com/u/ghoover"

# This API endpoint returns a JSON response with the results
# Search Help documentation
ENDPOINT_SEARCH = BASE_URL + '/search'

# This API endpoint returns a JSON string with the results
ENDPOINT_GET_ITEMS = BASE_URL + '/get-account-items'


GET_ITEMS = BASE_URL + "/get-account-items"

PARAMS_ITEMS_PER_PAGE = 50
PARAMS_PAGE_NUMBER = 1
# This is hardcoded to look at the first page of results
#  The default number of items per page is 50, so offset is calculated:
#   offset = page * 50
form_data = {'library_id': 77535, 'offset': PARAMS_ITEMS_PER_PAGE * PARAMS_PAGE_NUMBER}
# e.g. For page two, use the following line instead of above
# form_data = {'library_id': 77535, 'offset': 50}


data = requests.post(GET_ITEMS, data=form_data)

if data:
    print('Success!')

    # Convert string to Python dict
    results = json.loads(data.content)
    # print(results['item-info'])

    # Parse the HTML for the values of `<div class="item-title">TITLE HERE</div>`
    soup = BeautifulSoup(results['item-info'], "html.parser")
    titles = soup.find_all("div", "item-title")
    # print(titles)

    # Dictionary with {id: data-join-id, title: HTML_CONTENT}
    titles_dictionary = {}

    for t in titles:
      id = t.attrs.get("data-join-id", None)
      # If the ID is found, add to dictionary of results
      if id != "None":
        titles_dictionary[id] = t.contents

    print(titles_dictionary)

    # GREAT! Now add pagination to scrape until no more results…

else:
    print('Not Found.')