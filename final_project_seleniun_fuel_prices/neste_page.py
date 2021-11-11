from final_project_seleniun_fuel_prices.base_functions import BaseFunctions


class Neste(BaseFunctions):

    URL = "https://www.neste.lv/lv/content/degvielas-cenas"
    COOKIES = ".//button[@id='onetrust-accept-btn-handler']"
    V_PROD_LIST = ".//div[@class='field__item even']"

    def __init__(self):
        super().__init__(self.URL)

    def acpt_cookies(self):
        self.click(self.COOKIES)
        print("Cookies is accepted!")

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
    test_neste = Neste()
