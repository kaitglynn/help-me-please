```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep

class BrowserExtension:
    def __init__(self):
        self.options = Options()
        self.options.add_extension('path_to_extension.crx')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)

    def open_url(self, url):
        self.driver.get(url)

    def close_browser(self):
        self.driver.quit()

    def click_element(self, element_id):
        element = self.driver.find_element(By.ID, element_id)
        actions = ActionChains(self.driver)
        actions.click(element).perform()

    def send_keys(self, element_id, text):
        element = self.driver.find_element(By.ID, element_id)
        element.send_keys(text)

    def submit_form(self, element_id):
        element = self.driver.find_element(By.ID, element_id)
        element.submit()

if __name__ == "__main__":
    extension = BrowserExtension()
    extension.open_url('https://www.google.com')
    sleep(5)
    extension.close_browser()
```