from selenium.webdriver.support.wait import WebDriverWait

from package import base

class cookies(base):
        def cookies_btn(self):
            elem = WebDriverWait(, 10).until(
                EC.presence_of_element_located((By.XPATH, './/button[@id="onetrust-accept-btn-handler"]')))
            accept_btn_cookies = self.driver.find_element(By.XPATH, './/button[@id="onetrust-accept-btn-handler"]').click()
            print("We accepted Cookies")

