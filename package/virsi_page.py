from base import BaseFunctions


class VirsiA(BaseFunctions):
    COOKIES = ".//div[@class='actions']/child::a"
    V_PROD_LIST = ".//div[@class='banner-fuel-prices']"
    URL = "https://www.virsi.lv/lv/degvielas-cena"

    def __init__(self):
        super().__init__("https://www.virsi.lv/lv/degvielas-cena")
        self.acpt_cookie()
        self.v_95_price = self.virsi_k_get_95_price()
        self.v_dd_price = self.virsi_k_get_DD_price()
        self.quit()

    def acpt_cookie(self):
        self.click(self.COOKIES)
        print("Cookies accepted!")

    def virsi_k_get_95_price(self):
        prices_cirkle = self.get_price(self.V_PROD_LIST, 7, "95E", 8)
        print("95 price is: ", prices_cirkle)
        return prices_cirkle

    def virsi_k_get_DD_price(self):
        prices_cirkle = self.get_price(self.V_PROD_LIST, 0, "DD", 1)
        print("DD price is: ", prices_cirkle)
        return prices_cirkle

    def quit(self):
        self.driver.quit()


if __name__ == "__main__":
    test_virsi = VirsiA()
