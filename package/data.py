from virsi_page import VirsiA
from cirkle_page import CirkleK

def virsi_95():
    virsi_95 = VirsiA().v_95_price
    return virsi_95

def virsi_dd():
    virsi_dd = VirsiA().v_dd_price
    return virsi_dd

def cirkle_95():
    _95 = VirsiA().v_95_price
    return virsi_95

def cirkle_dd():
    virsi_dd = VirsiA().v_dd_price
    return virsi_dd

# def cirkle_95():
#     cirkle_95 = CirkleK().c_95_price
#     return cirkle_95


def data_export():

    with open('C:\\Users\\veigujul\\OneDrive - TietoEVRY\\Desktop\\dzeest\\Fuel_prices_test.csv', 'w') as f:
        headers = 'Fuel station, 95 price, DD price\n'
        f.write(headers)
        f.write(f"Virsi A, {virsi_95()}, {virsi_dd()}\n")
        # f.write(f"Cirkle K, {CirkleK().c_dd_price}\n")


if __name__ == "__main__":
    data_export()
