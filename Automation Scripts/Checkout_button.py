
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://qasvus.wixsite.com/ca-marketing")
driver.maximize_window()

driver.implicitly_wait(5)
wait = WebDriverWait(driver, 5)
wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@class='_3KzuS _3SQN-']")))
driver.find_element(By.ID, "comp-ksocy9ii2label").click()
driver.implicitly_wait(3)
driver.find_element(By.XPATH, "//*[text()='Product 1']").click()
driver.implicitly_wait(2)
wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@alt = 'Product 1']")))
driver.find_element(By.XPATH, "//*[@class = 'ColorPickerItem2577026692__radioInner']").click()
# add to cart
driver.find_element(By.CLASS_NAME, "buttonnext1749291004__content").click()

wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"_3N3nl")))

wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@value="1"]')))

#wait.until(EC.element_to_be_clickable(By.CLASS_NAME, "buttonnext1749291004__content"))

# Click on button "Add to Cart"
driver.find_element(By.CLASS_NAME, "buttonnext1749291004__content").click()
time.sleep(4)
# Switch to Frame "View Cart"
try:
    driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "_2DJg7"))
    print("Frame is switched to 'Cart'")
except NoSuchElementException:
    print("Failed to switch to frame")

driver.implicitly_wait(5)

try:
        driver.switch_to.frame(driver.find_element(By.NAME, 'tpaModal_rtby_x2zdo'))
        print("Frame is switched to 'Checkout'")
except NoSuchElementException:
        print("Frame did not switch")


try:
        wait = WebDriverWait(driver, 10)

        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@alt="iot_sq.png"]')))
        # verify button "Checkout"
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Checkout']")))
        # Checkout button is clickable
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Checkout']")))
        # # Click on Checkout that verify or is placed !
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Checkout']"))).click()
        print("All Elements is present and 'Checkout' button is OK")
except NoSuchElementException:
        print("Checkout is impossible!")




#//*[contains(text), "OrderSummary.headline”]


