from virsi_page import VirsiA
from cirkle_page import CirkleK
import datetime

def virsi_95():
    virsi_95 = VirsiA().v_95_price
    return virsi_95


def virsi_dd():
    virsi_dd = VirsiA().v_dd_price
    return virsi_dd


def cirkle_95():
    cirkle_95 = CirkleK().c_95_price
    return cirkle_95


def cirkle_dd():
    cirkle_dd = CirkleK().c_dd_price
    return cirkle_dd


def data_export():
    with open(f'Fuel_prices_test_{datetime.datetime.now().date()}.csv', 'w') as f:
        headers = 'Fuel station, 95 price, DD price, Date\n'
        f.write(headers)
        f.write(f"Virsi A, {virsi_95()}, {virsi_dd()}, {datetime.datetime.now()}\n")
        f.write(f"Cirkle K, {cirkle_95()}, {cirkle_dd()}, {datetime.datetime.now()}\n")


if __name__ == "__main__":
    data_export()
