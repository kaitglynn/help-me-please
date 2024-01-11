```python
import requests
from bs4 import BeautifulSoup

class ArticleResearch:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

    def get_article(self, url):
        response = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup

    def extract_content(self, soup):
        article_content = ''
        article = soup.find_all('p')
        for element in article:
            article_content += '\n' + ''.join(element.findAll(text = True))
        return article_content

    def research(self, url):
        soup = self.get_article(url)
        content = self.extract_content(soup)
        return content
```
This code defines a class `ArticleResearch` that can be used to scrape and extract content from scholarly articles. The `get_article` method sends a GET request to the provided URL and parses the HTML response using BeautifulSoup. The `extract_content` method then extracts the text content from all paragraph tags in the HTML. The `research` method combines these steps to scrape and extract content from a URL.