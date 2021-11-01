from final_project_seleniun_fuel_prices.base_functions import BaseFunctions


class VirsiA(BaseFunctions):
    URL = "https://www.virsi.lv/lv/degvielas-cena"
    COOKIES = ".//div[@class='actions']/child::a"
    V_PROD_LIST = ".//div[@class='banner-fuel-prices']"

    def __init__(self):
        super().__init__(self.URL)

    def acpt_cookie(self):
        self.click(self.COOKIES)
        print("Cookies is accepted!")

    def get_95_price(self):
        try:
            prices = float(self.get_price(self.V_PROD_LIST, 7, "95E", 8))
            print("95 price is: ", prices)
            return prices
        except:
            return print(list(enumerate(self.get_text(self.V_PROD_LIST))))

    def get_DD_price(self):
        try:
            prices = float(self.get_price(self.V_PROD_LIST, 0, "DD", 1))
            print("DD price is: ", prices)
            return prices
        except:
            return print(list(enumerate(self.get_text(self.V_PROD_LIST))))


if __name__ == "__main__":
    test_virsi = VirsiA()
