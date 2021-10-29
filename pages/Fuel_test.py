
from selenium import webdriver
from base_functions import BaseFunctions
from fuel_page import FuelPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class runTest():
    BaseFunctions.open_page(self=BaseFunctions, url= "https://www.neste.lv/lv/content/degvielas-cenas")
    BaseFunctions.click(self=BaseFunctions, by_locator='.//button[@id="onetrust-accept-btn-handler"]')
