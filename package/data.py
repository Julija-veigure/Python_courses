from virsi_page import VirsiA
from cirkle_page import CirkleK


def virsi_data():
    virsi = VirsiA()
    virsi_fuel_data = virsi.v_data
    return list(virsi_fuel_data)


def virsi_error():
    virsi = VirsiA()
    virsi_error = virsi.v_error
    return virsi_error


def cirkle_k_data():
    cirkle = CirkleK()
    cirkle_fuel_data = cirkle.c_data
    return list(cirkle_fuel_data)


def cirkle_k_error():
    cirkle = CirkleK()
    cirkle_error = cirkle.c_error
    return cirkle_error


def data_export():
    with open('C:\\Users\\veigujul\\OneDrive - TietoEVRY\\Desktop\\dzeest\\Fuel_prices.csv', 'w') as f:
        headers = 'Fuel station, 95 price, DD price, ERROR, \n'
        f.write(headers)
        f.write(f"Virsi A, {virsi_data()[1]}, {virsi_data()[3]}, {virsi_error()}\n")
        f.write(f"Cirkle K, {cirkle_k_data()[1]}, {cirkle_k_data()[3]}, {cirkle_k_error()}\n")


if __name__ == "__main__":
    cirkle_k_data()
    virsi_data()
    data_export()
