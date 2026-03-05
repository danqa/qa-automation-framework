import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_inventory_loads(page: Page):
    login = LoginPage(page)
    login.navigate()
    login.login_as("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    assert inventory.get_item_count() == 6

def test_add_item_to_cart(page: Page):
    login = LoginPage(page)
    login.navigate()
    login.login_as("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    inventory.add_first_item_to_cart()
    assert inventory.get_cart_count() == "1"