from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given("que esta en la pagina de login")
def navegador(context):
    context.driver = webdriver.Edge("C:/Users/javi1/Downloads/edgedriver/msedgedriver")
    context.driver.get("https://business.goasap.dev/")


@when('ingresa sus credenciales y presiona ingresar')
def login(context):
    context.driver.find_element(By.ID, "emailInput").send_keys("gundamthewitherofmercury@asap507.com")
    context.driver.find_element(By.ID, "exampleInputPassword1").send_keys("Q12345678")
    context.driver.find_element(By.XPATH, "/html/body/ngwork-root/asap-wizard-layout-login-activate/div/div/div[2]/ngwork-login/div/div/div[2]/div/div/form/div[3]/button/span").click()


@then('accede al business')
def business_succefull(context):
    succefull = context.driver

