from base import BaseFunctions


class VirsiA(BaseFunctions):
    COOKIES = ".//div[@class='actions']/child::a"
    V_PROD_LIST = ".//div[@class='banner-fuel-prices']"

    def __init__(self):
        super().__init__("https://www.virsi.lv/lv/degvielas-cena")
        self.acpt_cookie()
        self.v_data = self.get_virsi_produkt_list()
        self.v_error = self.error()
        self.quit()

    def acpt_cookie(self):
        self.click(self.COOKIES)
        print("Cookies accepted!")

    def get_virsi_produkt_list(self):
        all_data = self.get_text(self.V_PROD_LIST).split()
        if all_data[0] == "DD" and all_data[7] == "95E":
            virsi_95_name = 95
            virsi_95_price = float((all_data[8]))
            virsi_DD_name = "DD"
            virsi_DD_price = float((all_data[1]))
            print(virsi_95_name, virsi_95_price, virsi_DD_name, virsi_DD_price, "\n")
            return virsi_95_name, virsi_95_price, virsi_DD_name, virsi_DD_price
        else:
            return None

    def error(self):
        all_data = self.get_text(self.V_PROD_LIST).split()
        if all_data[0] != "DA" or all_data[7] != "95E":
            virsi_error = "In Virsi A page something was changed"
            print(virsi_error)
            return virsi_error
        else:
            None

    def quit(self):
        self.driver.quit()


if __name__ == "__main__":
    testVirsi = VirsiA()
