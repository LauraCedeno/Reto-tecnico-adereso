from utils.driver_setup import setup_driver, quit_driver
from pages.login_page import LoginPage
from pages.intenciones_page import IntencionesPage
import time

def before_feature(context, feature):
    print(f"Iniciando navegador para la Feature: {feature.name}")
    context.driver = setup_driver()
    context.login_page = LoginPage(context.driver)

    context.login_page.go_to_login()
    context.login_page.enter_email("laurayiselaca@gmail.com")
    context.login_page.enter_password("Adereso1906")
    context.login_page.click_login()
    print("Login completado para la Feature.")

def after_feature(context, feature):
    print(f"Finalizando navegador para la Feature: {feature.name}")
    time.sleep(10)
    quit_driver(context.driver)

def before_scenario(context, scenario):
    print(f"Iniciando escenario: {scenario.name}")
    context.intenciones_page = IntencionesPage(context.driver)

def after_scenario(context, scenario):
    print(f"Finalizando escenario: {scenario.name}")