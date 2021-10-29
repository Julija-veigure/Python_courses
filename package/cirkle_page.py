from base import BaseFunctions


class CirkleK(BaseFunctions):
    COOKIES = ".//a[@id='CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection']"
    V_PROD_LIST = ".//table[@border='0']"

    def __init__(self):
        super().__init__("https://www.circlek.lv/degvielas-cenas")
        self.acpt_cookie()
        self.c_data = self.get_cirkle_produkt_list()
        self.c_error = self.error()
        self.quit()

    def acpt_cookie(self):
        self.click(self.COOKIES)
        print("Cookies_accepted!")

    def get_cirkle_produkt_list(self):
        all_data = self.get_text(self.V_PROD_LIST).split()
        if all_data[7] == "95" and all_data[32] == "D":
            cirkle_95_name = 95
            cirkle_95_price = float((all_data[8]))
            cirkle_DD_name = "DD"
            cirkle_DD_price = float((all_data[33]))
            print(cirkle_95_name, cirkle_95_price, cirkle_DD_name, cirkle_DD_price, "\n")
            return cirkle_95_name, cirkle_95_price, cirkle_DD_name, cirkle_DD_price
        else:
            None


    def error(self):
        all_data = self.get_text(self.V_PROD_LIST).split()
        if all_data[7] != "95" or all_data[32] != "D":
            cirkle_error = "In Cirkle K page something was changed"
            print(cirkle_error)
            return cirkle_error
        else:
            None

    def quit(self):
        self.driver.quit()


if __name__ == "__main__":
    testCirkle = CirkleK()
