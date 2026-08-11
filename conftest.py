"""
conftest.py - Pytest Fixtures and HTML Report Configuration for GUVI Task 10
"""

import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    """
    Pytest fixture to initialize and yield a headless Chrome WebDriver.
    Ensures browser is closed cleanly after each test case.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    web_driver = webdriver.Chrome(options=chrome_options)
    web_driver.implicitly_wait(10)
    
    yield web_driver
    
    web_driver.quit()


def pytest_html_report_title(report):
    """
    Customizes the Pytest HTML Report Title.
    """
    report.title = "GUVI Zen Class - Task 10 Test Execution Report (SauceDemo Automation)"


def pytest_configure(config):
    """
    Adds custom metadata information to the Pytest HTML report header.
    """
    if hasattr(config, "_metadata"):
        config._metadata["Project Name"] = "SauceDemo Web Automation"
        config._metadata["Task"] = "GUVI Task 10"
        config._metadata["Tested URL"] = "https://www.saucedemo.com/"
        config._metadata["Tester"] = "Automated Test Suite (Selenium & Pytest)"
        config._metadata["Browser"] = "Headless Chrome"
