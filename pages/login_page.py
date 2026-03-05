from playwright.sync_api import Page, expect

class LoginPage:
    
    def __init__(self, page: Page):
        self.page = page
        # Define your locators here
        self.username_field = page.locator("#user-name")
        self.password_field = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator('[data-test="error"]')

    def navigate(self):
        self.page.goto("https://www.saucedemo.com")

    def login_as(self, username: str, password: str):
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()

    def get_error_message(self):
        return self.error_message