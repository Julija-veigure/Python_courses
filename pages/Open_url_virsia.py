import xlsxwriter
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class openPageVirsiA():
    driver = webdriver.Chrome()  # webdriver.Chrome()
    driver.get("https://www.virsi.lv/lv/degvielas-cena")
    print("Virši A page is opened")
    driver.maximize_window()
    elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, ".//div[@class='actions']/child::a")))
    accept_btn_cookies = driver.find_element(By.XPATH, ".//div[@class='actions']/child::a").click()
    print("We accepted Cookies")

    all_block = driver.find_element(By.XPATH, ".//div[@class='banner-fuel-prices']").text
    fuel = all_block.replace("Pērnavas iela 78, Rīga, LV-1009", "").split()
    print(fuel)
    # print(type(fuel))
    # driver.quit()

    if fuel[0] == "DD":
        dd = "DD"
        dd_price = float(fuel[1])
        e95 = "95E"
        e95_price = float(fuel[3])
        print(dd, dd_price)
        print(e95, e95_price)
    else:
        print("changes in fuel name")

# Neste_Futura_95 = driver.find_element(By.XPATH, ".//span[@style='font-size:14px;']/child::strong").text
# print(Neste_Futura_95)
# Neste_Futura_D = driver.find_element(By.XPATH, ".//span[@style='font-size:14px;']/child::strong").text
# print(Neste_Futura_D)

# file = "C:\Users\veigujul\OneDrive - TietoEVRY\Desktop\dzeest"
# # os.startfile(file)
# workbook = xlsxwriter.Workbook('hello.xlsx')
# worksheet = workbook.add_worksheet()
#
# # Use the worksheet object to write
# worksheet.write('A1', 'Hello..')
# worksheet.write('B1', 'Geeks')
# worksheet.write('C1', 'For')
# worksheet.write('D1', 'Geeks')
#
# # print("Test is DONE")
# # # data via the write() method.
