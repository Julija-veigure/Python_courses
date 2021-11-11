from final_project_seleniun_fuel_prices.base_functions import BaseFunctions


class CirkleK(BaseFunctions):

    COOKIES = ".//a[@id='CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection']"
    V_PROD_LIST = ".//table[@border='0']"
    URL = "https://www.circlek.lv/degvielas-cenas"

    def __init__(self):
        super().__init__(self.URL)

    def acpt_cookies(self):
        self.click(self.COOKIES)
        print("Cookies_accepted!")

    def get_95_price(self):
        try:
            price = float(self.get_price(self.V_PROD_LIST, "95"))
            print("95 price is: ", price)
            return price
        except:
            return print("Can't find fuel type - 95")

    def get_dd_price(self):
        try:
            price = float(self.get_price(self.V_PROD_LIST, "D"))
            print("DD price is: ", price)
            return price
        except:
            return print("Can't find fuel type - Diesel")


if __name__ == "__main__":
    test_cirkle = CirkleK()
