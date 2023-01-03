# Beautiful Soup Demo

This demo code is to show how to scrap paginated content from Libib (https://www.libib.com/u/ghoover).

The HTML response for this page does not contain the results. That data is requested after the page has been loaded by JQuery to an API endpoint, `/get-account-items`.

When the user scrolls to the bottom of the page, Javascript will trigger a load of more results (with the same `/get-account-items` endpoint mentioned above) and then automatically append them to the page. This is similar to social media "infinite scroll" UX.

The `libib_title_scraper.py` can be configured by changing the constants defined as `UPPERCASE_NAMES`.

## Installation

1. Install Python 3.x
2. Install Beautiful Soup

   `pip install beautifulsoup4`

3. Install `requests`

   `pip install requests`

## How to run

```
python libib_title_scraper.py
```

## TODO

- [ ] Iterate over paginated results to collect all data
- [ ] Implement script input for search terms to utilize `ENDPOINT_SEARCH`
