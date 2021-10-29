from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class baseFunctions():
    def open_age(self, url):
        self.driver = webdriver.Chrome() #webdriver.Chrome()
        self.driver.get(url)
        print("NESTE page is opened")
        self.driver.maximize_window()

