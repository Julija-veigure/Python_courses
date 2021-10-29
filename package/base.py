from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BaseFunctions:

    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        print(f"Opened page: {url}")
        self.driver.maximize_window()

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, by_locator))).click()

    def get_text(self, by_locator):
        element = self.driver.find_element(By.XPATH, by_locator).text
        print("Data was read from the page:")
        return element

    def get_list(self, by_locator):
        element_list = self.driver.find_elements(By.XPATH, by_locator)
        print(element_list)
        return element_list.text

# #if __name__ == "__main__":
#     open_page()
#     click()
#     get_text()
#     get_list()
