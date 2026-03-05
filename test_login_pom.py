import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_login_success(page: Page):
    login = LoginPage(page)
    login.navigate()
    login.login_as("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_login_locked_user(page: Page):
    login = LoginPage(page)
    login.navigate()
    login.login_as("locked_out_user", "secret_sauce")
    expect(login.get_error_message()).to_be_visible()