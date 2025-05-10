from behave import given, when, then
from pages.intenciones_page import IntencionesPage
import time

@given('el usuario está en la página principal')
def step_impl(context):
    context.intenciones_page = IntencionesPage(context.driver)

@when('el usuario navega a la sección de intenciones')
def step_impl(context):
    context.intenciones_page.go_to_intenciones()

@when('hace clic en el botón para crear una nueva intención')
def step_impl(context):
    context.intenciones_page.click_crear()

@when('completa el formulario con nombre "{nombre}", descripción "{descripcion}" y ejemplo "{ejemplo}"')
def step_impl(context, nombre, descripcion, ejemplo):
    context.intenciones_page.fill_form(nombre, descripcion, ejemplo)

@when('hace clic en el botón de guardar')
def step_impl(context):
    context.intenciones_page.click_guardar()

@then('debería ver la intención "{nombre}" en la lista')
def step_impl(context, nombre):
    assert context.intenciones_page.check_intent_in_list(nombre)



