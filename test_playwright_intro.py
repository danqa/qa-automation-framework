import pytest
from playwright.sync_api import Page, expect


@pytest.fixture
def login_page(page: Page):
    page.goto("https://www.saucedemo.com")
    return page

def test_login_success(login_page: Page):
    # Fill in credentials
    login_page.fill("#user-name", "standard_user")
    login_page.fill("#password", "secret_sauce")
    
    # Click login
    login_page.click("#login-button")

    # Assert we landed on the inventory page
    expect(login_page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_login_locked_user(login_page: Page):
    # Fill in credentials that are invalid
    login_page.fill("#user-name", "locked_out_user")
    login_page.fill("#password", "secret_sauce")

    # Click login
    login_page.click("#login-button")

    # assert error
    expect(login_page.locator('[data-test="error"]')).to_be_visible()