from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
import unittest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


#  User is able to switch to a Russian version
class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    # Methods in UnitTest should start from "test_" keyword
    def test_search(self):
        driver = self.driver
        driver.get("https://www.wikipedia.org/")
        driver.maximize_window()

        driver.implicitly_wait(5)
        wait = WebDriverWait(driver, 5)

        wait.until(EC.visibility_of_element_located((By.ID, "www-wikipedia-org")))
        driver.find_element(By.ID, "js-lang-list-button").click()
        driver.find_element(By.XPATH, '//*[@id="js-lang-lists"]/div[1]/ul/li[18]/a').click()
        driver.implicitly_wait(3)

        # opens Russian version
        WikiRUS = "https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0"
        assert driver.current_url == WikiRUS

        search = driver.find_element(By.XPATH, '//*[@id="searchInput"]')
        search.send_keys("Internet")
        driver.find_element(By.XPATH, '//*[@id="searchButton"]').click()

    def tearDown(self):
        self.driver.quit()


class FirefoxSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()

    # Methods in UnitTest should start from "test_" keyword
    def test_search(self):
        driver = self.driver
        driver.get("https://www.wikipedia.org/")
        driver.maximize_window()

        driver.implicitly_wait(5)
        wait = WebDriverWait(driver, 5)

        wait.until(EC.visibility_of_element_located((By.ID, "www-wikipedia-org")))
        driver.find_element(By.ID, "js-lang-list-button").click()
        driver.find_element(By.XPATH, '//*[@id="js-lang-lists"]/div[1]/ul/li[18]/a').click()
        driver.implicitly_wait(3)

        # opens Russian version
        WikiRUS = "https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0"
        assert driver.current_url == WikiRUS

        search = driver.find_element(By.XPATH, '//*[@id="searchInput"]')
        search.send_keys("Internet")
        driver.find_element(By.XPATH, '//*[@id="searchButton"]').click()

    def tearDown(self):
        self.driver.quit()
