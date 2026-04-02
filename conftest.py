import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage

@pytest.fixture
def login_page(page: Page):
    page.goto("https://www.saucedemo.com")
    return page

@pytest.fixture
def logged_in_page(page: Page):
    login = LoginPage(page)
    login.navigate()
    login.login_as("standard_user", "secret_sauce")
    return page
