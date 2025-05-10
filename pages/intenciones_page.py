from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class IntencionesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.url_intenciones = "https://broly.adere.so/vue/#/chatbots/27/intents"
        self.crear_button = (By.XPATH, "//span[text()='Añadir intención']")
        self.nombre_input_locator = (By.XPATH, '//input[@name="nombre"]')
        self.descripcion_input_locator = (By.XPATH, '//input[@name="descripcion"]')
        self.guardar_button = (By.XPATH, '//*[@id="app"]/div/div/div/div[3]/div/div[4]/div/button/span[4]')
        self.tabla_intenciones = (By.XPATH, "//table/tbody/tr")
        self.modal_locator = (By.XPATH, "//div[contains(@class, 'v-dialog')]")

    def go_to_intenciones(self):
        self.driver.get(self.url_intenciones)
        # Espera a que la tabla de intenciones tenga al menos una fila.
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located(self.tabla_intenciones))

    def click_crear(self):
        wait = WebDriverWait(self.driver, 20)
        crear_button = wait.until(EC.element_to_be_clickable(self.crear_button))
        crear_button.click()

    def fill_form(self, nombre, descripcion, ejemplo):
        wait = WebDriverWait(self.driver, 40)
        wait.until(EC.visibility_of_element_located(self.modal_locator)) # Espera a que el modal sea visible
        nombre_field = wait.until(EC.visibility_of_element_located(self.nombre_input_locator))
        nombre_field.send_keys(nombre)
        descripcion_field = wait.until(EC.visibility_of_element_located(self.descripcion_input_locator))
        descripcion_field.send_keys(descripcion)

    def click_guardar(self):
        wait = WebDriverWait(self.driver, 20)
        guardar_button = wait.until(EC.element_to_be_clickable(self.guardar_button))
        guardar_button.click()

    def check_intent_in_list(self, nombre):
        wait = WebDriverWait(self.driver, 20)
        wait.until(lambda driver: any(
            nombre.strip() in elem.text.strip()
            for elem in driver.find_elements(By.XPATH, "//table/tbody/tr/td[1]")
        ))

    def go_to_url(self, url):
        self.driver.get(url)
