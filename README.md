# QA Automation Framework

A Python-based test automation framework built with pytest and Playwright.

## Tech Stack
- Python 3.9
- pytest
- Playwright
- requests

## Test Coverage
- UI tests against SauceDemo e-commerce site
- API tests against JSONPlaceholder
- Page Object Model pattern

## Running Tests
# All tests
pytest -v

# UI tests only
pytest test_login_pom.py test_inventory.py -v

# API tests only
pytest test_api.py -v
