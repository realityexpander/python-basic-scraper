from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("starting scrapin'...")
browser = webdriver.Chrome()
browser.get('https://www.amazon.com/s?k=self+help+books&sprefix=self+help+%2C158&ref=nb_sb_ss_ts-doa-p_2_10')
time.sleep(5)

elements = browser.find_elements(By.XPATH, "//span[@class='a-size-base-plus a-color-base a-text-normal']")

for element in elements:
    print(element.text)
