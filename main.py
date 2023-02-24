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


def next_step_density():
    global init_pressure, init_temperature, init_density, reference_density
    if init_density < reference_density:
        init_pressure += 5
    elif init_density > reference_density:
        init_pressure -= 5
    return get_density(init_pressure, init_temperature)



print("Please enter the final parameters of chemical process (pressure and temperature)")
print("First enter pressure in bar")
pressure = input()
print("Now enter temperature in celsius degrees")
temperature = input()

driver = webdriver.Chrome()
reference_density = get_density(pressure, temperature)
print(
    f"The density at {pressure} bar and {temperature} celsius degrees is {reference_density} kilograms per cubic meter")

print("Please enter the initial temperature")
init_temperature = input()
init_pressure = 10
init_density = get_density(init_pressure, init_temperature)
print(f"The search for desired density will start from {init_pressure} bar with increment/decrement of 5")

cond = "y"
while cond:
    # initial loop to get near desired values of pressure
    while init_density < 0.8 * reference_density or init_density > 1.2 * reference_density:
        init_density = next_step_density()

    print(f"Found value of density is now {init_density} at {init_pressure} bar")
    print(f"Program is trying to find pressure at which density is {reference_density}")
    print("Do you wish to keep searching? If no, please press Enter, otherwise press any other key")
    cond = input()
    if not cond:
        break
    init_density = next_step_density()

print(f"The found value of pressure is {init_pressure} bar at which the density is {init_density}, which was selected "
      f"by user as close enough to desired value of {reference_density}")
