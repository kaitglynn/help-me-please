```python
import requests
from bs4 import BeautifulSoup

def scrape_web_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return None
    except Exception as err:
        print(f'Other error occurred: {err}')
        return None

    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def extract_data(soup, tag, attribute_name=None, attribute_value=None):
    if attribute_name and attribute_value:
        elements = soup.find_all(tag, {attribute_name: attribute_value})
    else:
        elements = soup.find_all(tag)

    extracted_data = [element.text for element in elements]
    return extracted_data
```