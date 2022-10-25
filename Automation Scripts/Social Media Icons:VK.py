from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://qasvus.wixsite.com/ca-marketing")
driver.maximize_window()

driver.implicitly_wait(5)
wait = WebDriverWait(driver, 5)
wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@ alt='VK Share']"))).click()

driver.implicitly_wait(7)

VK_link = "https://vk.com/qa_at_silicon_valley"
if driver.current_url != VK_link:
    print('Test Failed')

driver.quit()
