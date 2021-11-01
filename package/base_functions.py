from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BaseFunctions:

    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(url)
        print(f"Page is opened: {url}")

    def click(self, by_locator):
        """Click"""
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, by_locator))).click()

    def get_text(self, by_locator):
        """Get data/ text from page"""
        element = self.driver.find_element(By.XPATH, by_locator).text.split()
        return element

    def get_price(self, by_locator, numeration, fluel_name, fluel_price):
        """Get prices from the page"""
        all_data = self.get_text(by_locator)
        if all_data[numeration] == fluel_name:
            price = float((all_data[fluel_price]))
            print("Data was read from the page:")
            return price

    def close_page(self):
        self.driver.quit()
        print("Page is closed!\n")
