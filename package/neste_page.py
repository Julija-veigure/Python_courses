from base_functions import BaseFunctions


class Neste(BaseFunctions):
    URL = "https://www.neste.lv/lv/content/degvielas-cenas"
    COOKIES = ".//button[@id='onetrust-accept-btn-handler']"
    V_PROD_LIST = ".//div[@class='field__item even']"

    def __init__(self):
        super().__init__(self.URL)

    def acpt_cookie(self):
        self.click(self.COOKIES)
        print("Cookies is accepted!")

    def get_95_price(self):
        try:
            prices = float(self.get_price(self.V_PROD_LIST, 27, "95", 28))
            print("95 price is: ", prices)
            return prices
        except:
            return print(list(enumerate(self.get_text(self.V_PROD_LIST))))

    def get_DD_price(self):
        try:
            prices = float(self.get_price(self.V_PROD_LIST, 53, "D", 54))
            print("DD price is: ", prices)
            return prices
        except:
            return print(list(enumerate(self.get_text(self.V_PROD_LIST))))


if __name__ == "__main__":
    test_neste = Neste()
