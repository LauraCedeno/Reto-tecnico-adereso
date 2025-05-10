from selenium import webdriver

def setup_driver():
    # Configura tu navegador aquí (ejemplo con Chrome)
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def quit_driver(driver):
    if driver:
        driver.quit()