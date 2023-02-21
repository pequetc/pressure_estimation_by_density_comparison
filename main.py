from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.wolframalpha.com/')


def get_density(temperature, pressure):
    text_box = driver.find_element(By.XPATH, r'//*[@id="__next"]/div/div[1]/div/div/div[1]/section/form/div/div/input')
    text_box.send_keys(f'carbon dioxide density at {pressure} bar {temperature} celsius degrees')
    click_box = driver.find_element(By.XPATH, r'//*[@id="__next"]/div/div[1]/div/div/div[1]/section/form/span/button')
    click_box.click()
    time.sleep(5)
    data_box = driver.find_element(By.CSS_SELECTOR,
                                   r'#__next > div > div._1MeJ._3eup > main > div._3BQG > div._2ThP > div._pA1m > '
                                   r'section > section:nth-child(2) > div > div > img')
    search_outcome = data_box.get_attribute("alt")
    return search_outcome


read_data = get_density(20, 100)
print(read_data)
