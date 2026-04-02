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

def test_item_name_on_cart(logged_in_page: Page):
    inventory = InventoryPage(logged_in_page)
    
    # Get the first item name before adding to cart
    first_item_name = logged_in_page.locator(
        ".inventory_item_name"
    ).first.text_content()
    
    # Add it to cart
    inventory.add_first_item_to_cart()
    
    # Go to cart
    inventory.go_to_cart()
    
    # Assert the item name appears in the cart
    expect(logged_in_page.locator(
        ".cart_item .inventory_item_name"
    )).to_have_text(first_item_name)