# QA Automation Framework

![CI](https://github.com/danqa/qa-automation-framework/actions/workflows/tests.yml/badge.svg)

A Python-based test automation framework built with pytest and Playwright,
demonstrating real-world QA engineering practices.

## Tech Stack
- Python 3.9
- pytest
- Playwright
- requests

## Framework Structure
- Page Object Model (POM) pattern
- Shared fixtures via conftest.py
- Parametrized tests
- API and UI test separation

## Test Coverage
- UI tests against SauceDemo e-commerce site
  - Login success and failure scenarios
  - Inventory page validation
  - Add to cart flow
- API tests against JSONPlaceholder
  - Single resource retrieval
  - Collection retrieval
  - 404 handling

## Running Tests
# All tests
pytest -v

# UI tests only
pytest test_login_pom.py test_inventory.py -v

# API tests only
pytest test_api.py -v

# Run headed (watch the browser)
pytest test_login_pom.py -v --headed
