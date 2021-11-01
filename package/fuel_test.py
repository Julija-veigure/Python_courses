from virsi_page import VirsiA
from cirkle_page import CirkleK
from data_export import data_export
from neste_page import Neste


def fuel_test():
    virsi_a = VirsiA()
    virsi_a.acpt_cookie()
    v_95 = virsi_a.get_95_price()
    v_dd = virsi_a.get_DD_price()
    virsi_a.close_page()

    cirkle_k = CirkleK()
    cirkle_k.acpt_cookie()
    c_95 = cirkle_k.get_95_price()
    c_dd = cirkle_k.get_DD_price()
    cirkle_k.close_page()

    neste = Neste()
    neste.acpt_cookie()
    n_95 = neste.get_95_price()
    n_dd = neste.get_DD_price()
    neste.close_page()

    data_export(v_95, v_dd, c_95, c_dd, n_95, n_dd)


if __name__ == "__main__":
    fuel_test()
