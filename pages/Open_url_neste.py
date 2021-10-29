from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class open_page():
    driver = webdriver.Chrome() #webdriver.Chrome()
    driver.get("https://www.neste.lv/lv/content/degvielas-cenas")
    print("NESTE page is opened")
    driver.maximize_window()
# wait = driver.implicitly_wait(10)
# print("Waited...")
    elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, './/button[@id="onetrust-accept-btn-handler"]')))
    accept_btn_cookies = driver.find_element(By.XPATH, './/button[@id="onetrust-accept-btn-handler"]').click()
    print("We accepted Cookies")

    all_block = {driver.find_element(By.XPATH, ".//div[@class='field__item even']").text}
    #print(all_block)
    print(type(all_block))
    Neste_Futura_95 = driver.find_element(By.XPATH, ".//span[@style='font-size:14px;']/child::strong").text
    print(Neste_Futura_95)
    Neste_Futura_D = driver.find_element(By.XPATH, ".//span[@style='font-size:14px;']/child::strong").text
    print(Neste_Futura_D)
    driver.quit()
    print("Test is DONE")
