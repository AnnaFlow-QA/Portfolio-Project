
from selenium import webdriver
import unittest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()



driver.get("https://qasvus.wixsite.com/ca-marketing")
driver.set_window_size(1440, 807)
elements = driver.find_elements(By.CSS_SELECTOR, "#bgLayers_comp-ksocy8ov2 > .\\_3KzuS")
assert len(elements) > 0
elements = driver.find_elements(By.CSS_SELECTOR, "#SITE_HEADER .\\_1_UPn")
assert len(elements) > 0
driver.find_element(By.CSS_SELECTOR, ".\\_1UDJF").click()
element = driver.find_element(By.CSS_SELECTOR, ".\\_1UDJF")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.CSS_SELECTOR, "body")
actions = ActionChains(driver)
#actions.move_to_element(element, 0, 0).perform()
driver.find_element(By.XPATH, "//span[contains(text(),'Log In')]").click
driver.implicitly_wait(3)
driver.find_element(By.XPATH, '//*[@class="_3VCEv focus-within"]').click()
driver.implicitly_wait(3)

driver.find_element(By.ID, "input_input_emailInput_SM_ROOT_COMP16").click()
driver.find_element(By.ID, "input_input_emailInput_SM_ROOT_COMP16").send_keys("lavazzanna85@gmail.com")
driver.find_element(By.ID, "input_input_passwordInput_SM_ROOT_COMP16").click()
driver.find_element(By.ID, "input_input_passwordInput_SM_ROOT_COMP16").send_keys("Kjelka_7")
driver.find_element(By.CSS_SELECTOR, "#okButton_SM_ROOT_COMP16 > .\\_1fbEI").click()

driver.quit()