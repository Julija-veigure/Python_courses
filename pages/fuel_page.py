from selenium.webdriver.common.by import By

from base_functions import BaseFunctions
#
#


class FuelPage(BaseFunctions):

   # COOKIE = './/button[@id="onetrust-accept-btn-handler"]'
    def close_cookies(self, by_locator):
          BaseFunctions.click(By.XPATH, './/button[@id="onetrust-accept-btn-handler"]')

#     def open_page(self):


