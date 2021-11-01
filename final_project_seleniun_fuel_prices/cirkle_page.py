from final_project_seleniun_fuel_prices.base_functions import BaseFunctions


class CirkleK(BaseFunctions):
    COOKIES = ".//a[@id='CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection']"
    V_PROD_LIST = ".//table[@border='0']"
    URL = "https://www.circlek.lv/degvielas-cenas"

    def __init__(self):
        super().__init__(self.URL)

    def acpt_cookie(self):
        self.click(self.COOKIES)
        print("Cookies_accepted!")

    def get_95_price(self):
        try:
            prices = float(self.get_price(self.V_PROD_LIST, 7, "95", 8))
            print("95 price is: ", prices)
            return prices
        except:
            return print(list(enumerate(self.get_text(self.V_PROD_LIST))))

    def get_DD_price(self):
        try:
            prices = float(self.get_price(self.V_PROD_LIST, 22, "D", 23))
            print("DD price is: ", prices)
            return prices
        except:
            return print(list(enumerate(self.get_text(self.V_PROD_LIST))))


if __name__ == "__main__":
    test_cirkle = CirkleK()
