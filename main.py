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
time.sleep(10)
data_box = driver.find_element(By.CSS_SELECTOR, r'#__next > div > div._1MeJ._3eup > main > div._3BQG > div._2ThP > div._pA1m > section > section:nth-child(2) > div > div > img')
time.sleep(5)









