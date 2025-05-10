from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def click(self, by, value):
        self.find_element(by, value).click()

    def send_keys(self, by, value, text):
        self.find_element(by, value).send_keys(text)

    def get_text(self, by, value):
        return self.find_element(by, value).text

    def is_element_present(self, by, value):
        try:
            self.find_element(by, value)
            return True
        except:
            return False