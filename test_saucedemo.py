"""
test_saucedemo.py - Pytest Test Cases for SauceDemo Automation (GUVI Task 10)
-----------------------------------------------------------------------------
Test Suite includes Positive and Negative test cases for:
1. Title of web application
2. URL of the Homepage
3. URL of the Dashboard after Login with valid/invalid credentials
4. Extraction of webpage content into "Webpage_task_11.txt"
"""

import os
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com/"
EXPECTED_TITLE = "Swag Labs"
EXPECTED_HOMEPAGE_URL = "https://www.saucedemo.com/"
EXPECTED_DASHBOARD_URL = "https://www.saucedemo.com/inventory.html"
WEBPAGE_CONTENT_FILE = "Webpage_task_11.txt"


class TestSauceDemoTitle:
    """
    Test suite for verifying the Web Application Title (Positive & Negative).
    """

    def test_title_positive(self, driver):
        """
        [Positive Test] Verify that the webpage title matches 'Swag Labs'.
        """
        driver.get(BASE_URL)
        actual_title = driver.title
        
        # Assertion: Title should match expected title
        assert actual_title == EXPECTED_TITLE, (
            f"Expected title '{EXPECTED_TITLE}', but got '{actual_title}'"
        )
        print(f"\n[PASS] Title Positive Test: Webpage title is '{actual_title}'")

    def test_title_negative(self, driver):
        """
        [Negative Test] Verify that the webpage title does NOT match an incorrect string.
        """
        driver.get(BASE_URL)
        actual_title = driver.title
        incorrect_title = "Incorrect Title - E-Commerce App"
        
        # Assertion: Title should NOT equal wrong title or empty string
        assert actual_title != incorrect_title, (
            f"Title should not equal '{incorrect_title}'"
        )
        assert actual_title != "", "Title should not be empty"
        print(f"\n[PASS] Title Negative Test: Title '{actual_title}' successfully differs from '{incorrect_title}'")


class TestSauceDemoHomepageURL:
    """
    Test suite for verifying the Homepage URL (Positive & Negative).
    """

    def test_homepage_url_positive(self, driver):
        """
        [Positive Test] Verify that navigating to base URL loads the correct homepage URL.
        """
        driver.get(BASE_URL)
        actual_url = driver.current_url
        
        # Assertion: Current URL should match expected homepage URL
        assert actual_url == EXPECTED_HOMEPAGE_URL, (
            f"Expected URL '{EXPECTED_HOMEPAGE_URL}', but got '{actual_url}'"
        )
        print(f"\n[PASS] Homepage URL Positive Test: Current URL is '{actual_url}'")

    def test_homepage_url_negative(self, driver):
        """
        [Negative Test] Verify that the Homepage URL is NOT pointing to an unauthenticated dashboard URL.
        """
        driver.get(BASE_URL)
        actual_url = driver.current_url
        incorrect_url = "https://www.saucedemo.com/inventory.html"
        
        # Assertion: Homepage URL should NOT equal dashboard URL before login
        assert actual_url != incorrect_url, (
            f"Homepage URL should not be redirected to '{incorrect_url}' without login"
        )
        print(f"\n[PASS] Homepage URL Negative Test: Homepage URL '{actual_url}' is not '{incorrect_url}'")


class TestSauceDemoDashboardURL:
    """
    Test suite for verifying Dashboard URL after Login and content extraction (Positive & Negative).
    """

    def test_dashboard_url_positive(self, driver):
        """
        [Positive Test] Verify successful login with valid credentials (standard_user / secret_sauce),
        verify redirect to Dashboard URL (inventory.html), and extract full page content into 'Webpage_task_11.txt'.
        """
        driver.get(BASE_URL)
        
        # Locate input fields and submit button
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")
        
        # Enter valid credentials
        username_field.send_keys("standard_user")
        password_field.send_keys("secret_sauce")
        login_button.click()
        
        # Wait for inventory list to confirm successful login
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        )
        
        actual_dashboard_url = driver.current_url
        
        # Assertion 1: Check dashboard URL
        assert actual_dashboard_url == EXPECTED_DASHBOARD_URL, (
            f"Expected Dashboard URL '{EXPECTED_DASHBOARD_URL}', but got '{actual_dashboard_url}'"
        )
        
        # Task Step 3: Extract entire contents of webpage after login & save to text file
        page_source = driver.page_source
        with open(WEBPAGE_CONTENT_FILE, "w", encoding="utf-8") as f:
            f.write(page_source)
            
        # Assertion 2: Verify file is created and non-empty
        assert os.path.exists(WEBPAGE_CONTENT_FILE), (
            f"File '{WEBPAGE_CONTENT_FILE}' was not created"
        )
        assert os.path.getsize(WEBPAGE_CONTENT_FILE) > 0, (
            f"File '{WEBPAGE_CONTENT_FILE}' is empty"
        )
        
        print(f"\n[PASS] Dashboard URL Positive Test: Redirected to '{actual_dashboard_url}'")
        print(f"[PASS] Extracted {len(page_source)} characters of webpage content to '{WEBPAGE_CONTENT_FILE}'")

    def test_dashboard_url_negative(self, driver):
        """
        [Negative Test] Verify that logging in with invalid credentials fails,
        does NOT navigate to Dashboard URL (inventory.html), and displays an error message.
        """
        driver.get(BASE_URL)
        
        # Locate input fields and submit button
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")
        
        # Enter invalid credentials
        username_field.send_keys("invalid_user")
        password_field.send_keys("wrong_password")
        login_button.click()
        
        # Wait for error message container
        error_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
        )
        error_text = error_element.text
        actual_url = driver.current_url
        
        # Assertion 1: Current URL should NOT be the Dashboard URL
        assert actual_url != EXPECTED_DASHBOARD_URL, (
            f"URL should not be '{EXPECTED_DASHBOARD_URL}' on failed login"
        )
        
        # Assertion 2: User should remain on homepage URL
        assert actual_url == EXPECTED_HOMEPAGE_URL, (
            f"Expected user to remain on '{EXPECTED_HOMEPAGE_URL}', but was on '{actual_url}'"
        )
        
        # Assertion 3: Error message should be visible and contain expected text
        assert "Epic sadface:" in error_text, (
            f"Expected error message containing 'Epic sadface:', but got '{error_text}'"
        )
        
        print(f"\n[PASS] Dashboard URL Negative Test: Login failed as expected with error: '{error_text}'")
        print(f"[PASS] User remained on homepage URL '{actual_url}' and was not redirected to dashboard")
