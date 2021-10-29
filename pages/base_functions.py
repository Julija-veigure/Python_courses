from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseFunctions():

    def open_page(self, url):
        self.driver = webdriver.ChromiumDriver
        self.get(url)

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator)).click

    def get_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        return element.text

    def get(self, url):
        self.driver.get(url)
