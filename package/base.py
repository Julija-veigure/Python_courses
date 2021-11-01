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

    # def __init__(self):
    #     self.driver = webdriver.Chrome()
    #
    # def open_page(self,url):
    #     self.driver.get(url)
    #     print(f"Opened page: {url}")
    #     self.driver.maximize_window()

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, by_locator))).click()

    def get_text(self, by_locator):
        element = self.driver.find_element(By.XPATH, by_locator).text
        return element

    # def get_list(self, by_locator):
    #     element_list = self.driver.find_elements(By.XPATH, by_locator)
    #     print(element_list)
    #     return element_list.text

    def get_price(self, by_locator, numeration, fluel_name, fluel_price):
        """by_locator, dd_numeration, dd_name, e95_numeration, e95_name, dd_price, e95_price"""
        all_data = self.get_text(by_locator).split()
        # print(numeration.all_data)
        if all_data[numeration] == fluel_name:
            price = float((all_data[fluel_price]))
            print("Data was read from the page:")
            return price
        else:
            error = "ERROR"
            return error



    # def get_list(self, by_locator, dd_numeration, dd_name, e95_numeration, e95_name, dd_price, e95_price):
    #     """by_locator, dd_numeration, dd_name, e95_numeration, e95_name, dd_price, e95_price"""
    #     all_data = self.get_text(by_locator).split()
    #     if all_data[dd_numeration] == dd_name and all_data[e95_numeration] == e95_name:
    #         DD_price = float((all_data[dd_price]))
    #         e95_price = float((all_data[e95_price]))
    #         print("Data was read from the page:")
    #         return [e95_price, DD_price]
    #     else:
    #         error = "error"
    #         return error



# #if __name__ == "__main__":
#     open_page()
#     click()
#     get_text()
#     get_list()

