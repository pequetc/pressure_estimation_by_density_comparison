from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from urllib.request import urlopen

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

print("Please enter desired pressure for estimation")
pressure = 2
    #input()
print("Please enter desired temperature for estimation")
temperature = 2
    #input()

driver = webdriver.Chrome()
driver.get('https://www.wolframalpha.com/')

text_box = driver.find_element(By.XPATH, r'//*[@id="__next"]/div/div[1]/div/div/div[1]/section/form/div/div/input')
text_box.send_keys(f'carbon dioxide density at {pressure} bar {temperature} celsius degrees')
click_box = driver.find_element(By.XPATH, r'//*[@id="__next"]/div/div[1]/div/div/div[1]/section/form/span/button')
click_box.click()
time.sleep(5)
data_box = driver.find_element(By.XPATH, r'//*[@id="__next"]/div/div[1]/main/div[2]/div[2]/div[2]/section/section[3]/div[1]/div/button/span')
data_box.click()
time.sleep(5)









