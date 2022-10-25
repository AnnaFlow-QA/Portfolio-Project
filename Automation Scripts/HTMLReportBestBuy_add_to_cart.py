from ast import main

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import HtmlTestRunner

from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get("https://www.bestbuy.com/")
driver.set_window_size(1440, 807)
elements = driver.find_elements(By.CSS_SELECTOR, ".top-nav")
assert len(elements) > 0
elements = driver.find_elements(By.CSS_SELECTOR, ".bottom-nav")
assert len(elements) > 0
driver.find_element(By.CSS_SELECTOR, ".bottom-left-links .v-p-top-xxs").click()
driver.find_element(By.LINK_TEXT, "Black Friday Deals Right Now").click()
driver.execute_script("window.scrollTo(0,2)")
driver.execute_script("window.scrollTo(0,220)")
driver.execute_script("window.scrollTo(0,245)")
driver.execute_script("window.scrollTo(0,352)")
driver.execute_script("window.scrollTo(0,448)")
driver.execute_script("window.scrollTo(0,502)")
driver.execute_script("window.scrollTo(0,611)")
driver.execute_script("window.scrollTo(0,892)")
driver.execute_script("window.scrollTo(0,1062)")
driver.execute_script("window.scrollTo(0,1326)")
element =driver.find_element(By.CSS_SELECTOR,
                                           "#wf-offer-33d9c663-8805-4aaf-8ee9-69c89cbd13f3 .wf-offer-image > .wf-offer-link")
actions = ActionChains(driver)

element = driver.find_element(By.CSS_SELECTOR, "body")
actions = ActionChains(driver)
#actions.move_to_element(element, 0, 0).perform()
element = driver.find_element(By.CSS_SELECTOR, "#wf-offer-33d9c663-8805-4aaf-8ee9-69c89cbd13f3 .wf-image")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.find_element(By.CSS_SELECTOR, "#wf-offer-33d9c663-8805-4aaf-8ee9-69c89cbd13f3 .wf-image").click()
driver.execute_script("window.scrollTo(0,1)")
driver.execute_script("window.scrollTo(0,76)")
driver.execute_script("window.scrollTo(0,271)")
element = driver.find_element(By.CSS_SELECTOR, ".item:nth-child(3) .variation-carousel-tile")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.CSS_SELECTOR, "body")
actions = ActionChains(driver)
#actions.move_to_element(element, 0, 0).perform()
driver.find_element(By.CSS_SELECTOR, ".item:nth-child(3) .tile-image").click()
element = driver.find_element(By.CSS_SELECTOR, ".primary-button")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.CSS_SELECTOR, "body")
actions = ActionChains(driver)
#actions.move_to_element(element, 0, 0).perform()
driver.execute_script("window.scrollTo(0,64)")
driver.execute_script("window.scrollTo(0,165)")
driver.execute_script("window.scrollTo(0,456)")
driver.execute_script("window.scrollTo(0,691)")
element = driver.find_element(By.CSS_SELECTOR, ".primary-button")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.CSS_SELECTOR, "body")
actions = ActionChains(driver)
#actions.move_to_element(element, 0, 0).perform()
element = driver.find_element(By.CSS_SELECTOR, ".c-button-primary")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.find_element(By.CSS_SELECTOR, ".c-button-primary").click()
element = driver.find_element(By.CSS_SELECTOR, "body")
actions = ActionChains(driver)
#actions.move_to_element(element, 0, 0).perform()
driver.implicitly_wait(3)
element = driver.find_element(By.LINK_TEXT, "Go to Cart")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.find_element(By.LINK_TEXT, "Go to Cart").click()
driver.implicitly_wait(2)

if "Cart - Best Buy" in driver.title:
    print("Test passed")

element = driver.find_element(By.CSS_SELECTOR, ".pricing-basic-banner")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element(By.CSS_SELECTOR, "body")
actions = ActionChains(driver)
#move_to_element(element, 0, 0).perform()
driver.execute_script("window.scrollTo(0,2)")
driver.execute_script("window.scrollTo(0,164)")

driver.quit()

if __name__ != '__main__':
    pass
else:
    main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./HtmlReports'))


