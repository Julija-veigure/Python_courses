from final_project_seleniun_fuel_prices.base_functions import BaseFunctions


class VirsiA(BaseFunctions):

    URL = "https://www.virsi.lv/lv/degvielas-cena"
    COOKIES = ".//div[@class='actions']/child::a"
    V_PROD_LIST = ".//div[@class='banner-fuel-prices']"

    def __init__(self):
        super().__init__(self.URL)

    def acpt_cookies(self):
        self.click(self.COOKIES)
        print("Cookies is accepted!")

    def get_95_price(self):
        try:
            price = float(self.get_price(self.V_PROD_LIST, "95E"))
            print("95 price is: ", price)
            return price
        except:
            return print("Can't find fuel type - 95")

    def get_dd_price(self):
        try:
            price = float(self.get_price(self.V_PROD_LIST, "DD"))
            print("DD price is: ", price)
            return price
        except:
            return print("Can't find fuel type - Diesel")


if __name__ == "__main__":
    test_virsi = VirsiA()
