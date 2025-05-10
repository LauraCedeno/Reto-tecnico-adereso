from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.email_field = (By.XPATH, "//input[@id='input-1']")
        self.password_field = (By.XPATH, "//input[@id='input-3']")
        self.login_button = (By.XPATH, '//*[@id="app"]/div/div/div/section/div[1]/form/button')
        self.capcha_iframe_selector = (By.XPATH, "//iframe[contains(@title, 'reCAPTCHA')]")
        self.capcha_checkbox_selector = (By.XPATH, "//span[@id='recaptcha-anchor']/div[1]")


    def go_to_login(self):
        self.driver.get("https://broly.adere.so/vue/#/login")

    def enter_email(self, email):
        self.send_keys(*self.email_field, email)

    def enter_password(self, password):
        self.send_keys(*self.password_field, password)

    def click_login(self):
        self.click(*self.login_button)
        try:
            wait = WebDriverWait(self.driver, 20)  # Aumenta el tiempo de espera a 20 segundos
            iframe = wait.until(EC.presence_of_element_located(self.capcha_iframe_selector))
            self.driver.switch_to.frame(iframe)
            checkbox = wait.until(EC.presence_of_element_located(self.capcha_checkbox_selector))
            checkbox.click()
            self.driver.switch_to.default_content()
            print("Se intentó interactuar con el CAPTCHA.")
        except (NoSuchElementException, TimeoutException) as e:
            print(f"No se pudo interactuar con el CAPTCHA (NoSuchElement/Timeout): {e}")
        except Exception as e:
            print(f"Ocurrió otro error al intentar interactuar con el CAPTCHA: {e}")