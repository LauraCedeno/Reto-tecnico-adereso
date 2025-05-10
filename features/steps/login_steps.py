from behave import given, when, then
from pages.login_page import LoginPage

@given('el usuario está en la página de login')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.go_to_login()

@when('el usuario ingresa su correo "{email}" y contraseña "{password}"')
def step_impl(context, email, password):
    context.login_page.enter_email(email)
    context.login_page.enter_password(password)

@when('hace clic en el botón de iniciar sesión')
def step_impl(context):
    context.login_page.click_login()

@then('debería ver la página principal')
def step_impl(context):
    assert "dashboard" in context.driver.current_url.lower()