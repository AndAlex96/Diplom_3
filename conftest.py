from selenium import webdriver
import pytest
from helpers.urls import BASE_URL, URL_AUTH_USER, URL_AUTH_REGISTER
import requests
from helpers.auxiliary_functions_for_api import generate_email_password_name

@pytest.fixture
def created_user():
    email, password, name = generate_email_password_name()
    payload = {"email": email, "password": password, "name": name}
    response = requests.post(url=URL_AUTH_REGISTER, data=payload)
    response_body = response.json()
    get_token_access = response_body.get('accessToken')
    yield email, password, name
    requests.delete(url=URL_AUTH_USER, data=get_token_access)

@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get(BASE_URL)

    yield browser

    browser.quit()