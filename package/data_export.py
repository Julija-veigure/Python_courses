import datetime


def data_export(virsi95, virsidd, cirkle95, cirkledd, neste95, nestedd):
    with open(f'C:\\Users\\veigujul\\OneDrive - TietoEVRY\\Desktop\\dzeest\\'
              f'Fuel_prices_test_{datetime.datetime.now().date()}.csv', 'w') as f:
        headers = 'Fuel station, 95 price, DD price, Date\n'
        f.write(headers)
        f.write(f"Virsi A, {virsi95}, {virsidd}, {datetime.datetime.now()}\n")
        f.write(f"Cirkle K, {cirkle95}, {cirkledd}, {datetime.datetime.now()}\n")
        f.write(f"Neste, {neste95}, {nestedd}, {datetime.datetime.now()}\n")
        print("Data is exported.\nTest is DONE!")


if __name__ == "__main__":
    data_export()
