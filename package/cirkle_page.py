from base import BaseFunctions


class CirkleK(BaseFunctions):
    COOKIES = ".//a[@id='CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection']"
    V_PROD_LIST = ".//table[@border='0']"

    def __init__(self):
        super().__init__("https://www.circlek.lv/degvielas-cenas")
        self.acpt_cookie()
        self.c_95_price = self.cirkle_k_get_95_price()
        self.c_dd_price = self.cirkle_k_get_DD_price()
        self.quit()

    def acpt_cookie(self):
        self.click(self.COOKIES)
        print("Cookies_accepted!")

    def cirkle_k_get_95_price(self):
        prices_cirkle = self.get_price(self.V_PROD_LIST, 7, "95", 8)
        print("95 price is: ", prices_cirkle)
        return prices_cirkle

    def cirkle_k_get_DD_price(self):
        prices_cirkle = self.get_price(self.V_PROD_LIST, 22, "D", 23)
        print("DD price is: ", prices_cirkle)
        return prices_cirkle

    def quit(self):
        self.driver.quit()


if __name__ == "__main__":
    test_cirkle = CirkleK()
