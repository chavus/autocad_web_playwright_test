import pytest
from playwright.sync_api import Page
from autocad_app.login_page import Login
from autocad_app.home_page import Home
import os
from dotenv import load_dotenv

"""
The conftest.py file serves as a means of providing fixtures for an entire directory. 
Fixtures defined in a conftest.py can be used by any test in that package without needing to import them 
(pytest will automatically discover them).
"""

load_dotenv()
USERNAME = os.getenv('APP_USERNAME')
PASSWORD = os.getenv('APP_PASSWORD')


@pytest.fixture(name='logged_in_page')
def log_in(page: Page):
    """Goes through the login process

    :param page: Playwright Page object
    :return: a page after login
    """
    page.goto('/')
    Login(page).sign_in(USERNAME, PASSWORD)
    Home(page).wait_for()
    # page.wait_for_url(test_properties.HOME_URL)
    yield page






