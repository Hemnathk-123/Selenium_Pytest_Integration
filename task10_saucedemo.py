"""
GUVI Zen Class - Task 10 Automation Script
-------------------------------------------
Task Requirements:
1. Visit URL: https://www.saucedemo.com/
2. Login with credentials:
   - Username: standard_user
   - Password: secret_sauce
3. Fetch:
   a) Title of the webpage
   b) Current URL of the webpage
   c) Extract entire contents of the webpage and save it in "Webpage_task_11.txt"
"""

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def create_headless_chrome_driver():
    """
    Initializes and returns a headless Chrome Selenium WebDriver instance.
    Configured for headless execution in sandbox/CI environments.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    return driver


def fetch_title(driver):
    """
    Fetches and returns the title of the current webpage.
    """
    title = driver.title
    print(f"[INFO] Webpage Title: {title}")
    return title


def fetch_current_url(driver):
    """
    Fetches and returns the current URL of the webpage.
    """
    url = driver.current_url
    print(f"[INFO] Current Webpage URL: {url}")
    return url


def perform_login(driver, username, password):
    """
    Performs login action on https://www.saucedemo.com/ using provided credentials.
    """
    print(f"[INFO] Navigating to login page...")
    driver.get("https://www.saucedemo.com/")
    
    # Locate elements
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")
    
    # Perform login
    username_field.clear()
    username_field.send_keys(username)
    password_field.clear()
    password_field.send_keys(password)
    login_button.click()
    
    # Wait for dashboard inventory container
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )
    print(f"[SUCCESS] Login successful for user: {username}")


def save_webpage_content(driver, output_filename="Webpage_task_11.txt"):
    """
    Extracts the entire HTML content/source of the current webpage and saves it to a text file.
    """
    page_content = driver.page_source
    with open(output_filename, "w", encoding="utf-8") as file:
        file.write(page_content)
    
    print(f"[SUCCESS] Extracted webpage content saved to '{output_filename}' ({len(page_content)} bytes)")
    return output_filename


def main():
    """
    Main function executing the Task 10 workflow.
    """
    print("==================================================")
    print("        GUVI Task 10 - SauceDemo Automation      ")
    print("==================================================")
    
    driver = create_headless_chrome_driver()
    
    try:
        # Step 1: Visit SauceDemo URL
        driver.get("https://www.saucedemo.com/")
        
        # Step 2: Fetch Title & Current URL before login
        homepage_title = fetch_title(driver)
        homepage_url = fetch_current_url(driver)
        
        # Step 3: Login with standard_user credentials
        perform_login(driver, "standard_user", "secret_sauce")
        
        # Step 4: Fetch Dashboard URL after login
        dashboard_title = fetch_title(driver)
        dashboard_url = fetch_current_url(driver)
        
        # Step 5: Save entire contents to Webpage_task_11.txt
        save_webpage_content(driver, "Webpage_task_11.txt")
        
        print("\n[SUMMARY]")
        print(f" - Homepage Title: {homepage_title}")
        print(f" - Homepage URL:   {homepage_url}")
        print(f" - Dashboard Title: {dashboard_title}")
        print(f" - Dashboard URL:  {dashboard_url}")
        print("==================================================")
        
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
