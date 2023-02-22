from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def get_density(pressure, temperature):
    driver.get('https://www.wolframalpha.com/')
    text_box = driver.find_element(By.XPATH, r'//*[@id="__next"]/div/div[1]/div/div/div[1]/section/form/div/div/input')
    text_box.send_keys(f'carbon dioxide density at {pressure} bar {temperature} celsius degrees')
    click_box = driver.find_element(By.XPATH, r'//*[@id="__next"]/div/div[1]/div/div/div[1]/section/form/span/button')
    click_box.click()
    time.sleep(5)
    data_box = driver.find_element(By.CSS_SELECTOR,
                                   r'#__next > div > div._1MeJ._3eup > main > div._3BQG > div._2ThP > div._pA1m > '
                                   r'section > section:nth-child(2) > div > div > img')
    search_outcome = convert_density(data_box.get_attribute("alt"))
    return search_outcome


def convert_density(str):
    list = str.split(" ")
    return float(list[0])


print("Please enter the final parameters of chemical process (pressure and temperature)")
print("First enter pressure in bar")
pressure = input()
print("Now enter temperature in celsius degrees")
temperature = input()

driver = webdriver.Chrome()
reference_density = get_density(pressure, temperature)
print(f"The density at {pressure} bar and {temperature} celsius degrees is {reference_density} kilograms per cubic metre")

print("Please enter the initial temperature")
init_temperature = input()
init_pressure = 10
init_density = get_density(init_pressure, init_temperature)

cond = "y"
while cond:
    print(f"Found value of density is now {init_density}")
    print("Do you wish to keep searching? If no, please press Enter, otherwise press any other key")
    increment = 5
    print(f"The pressure will start from 10 bar and increment by {increment} (which is equal 5 by default). Do you "
          f"wish to enter another value of increment?")
    cond = input()
    if not cond:
        break
    if init_density < reference_density:
        init_pressure += 5
    elif init_density > reference_density:
        init_pressure -= 5
    init_density = get_density(init_pressure, init_temperature)
