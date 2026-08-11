# GUVI Zen Class - Task 10: SauceDemo Selenium Automation & Pytest Testing

This repository contains the complete implementation for **Task 10 (SauceDemo Automation)** as required by GUVI.

---

## 📌 Task Description

### Target Web Application
- **URL**: `https://www.saucedemo.com/`
- **Credentials**:
  - **Username**: `standard_user`
  - **Password**: `secret_sauce`

### Tasks Performed
1. **Automation Script (`task10_saucedemo.py`)**:
   - Fetches the **Title** of the webpage before and after login.
   - Fetches the **Current URL** of the webpage before and after login.
   - Logs into the application with valid credentials.
   - Extracts the entire HTML content of the page after login and saves it to a text file named `Webpage_task_11.txt`.

2. **Pytest Test Suite (`test_saucedemo.py`)**:
   - Implements **Positive** and **Negative** test cases for:
     1. Title of Web Application
     2. URL of Homepage
     3. URL of Dashboard after Login
   - Generates a self-contained **HTML Test Report** using `pytest-html`.

---

## 📁 Repository & Project Structure

```
.
├── task10_saucedemo.py       # Standalone Python automation script
├── test_saucedemo.py         # Pytest test suite with Positive & Negative tests
├── conftest.py               # Pytest configuration & browser fixtures
├── Webpage_task_11.txt       # Extracted webpage content (Task requirement)
├── reports/
│   └── report.html           # Generated Pytest HTML Report
├── requirements.txt          # Python dependencies
├── .gitignore                # Git ignore configuration
└── README.md                 # Project documentation
```

---

## 🧪 Test Case Coverage

| Category | Test Case Name | Test Description | Expected Result |
| :--- | :--- | :--- | :--- |
| **Title** | `test_title_positive` | Verify application title on homepage | Title equals `"Swag Labs"` |
| **Title** | `test_title_negative` | Verify application title is not invalid | Title does NOT equal `"Incorrect Title"` |
| **Homepage URL** | `test_homepage_url_positive` | Verify current URL on navigating to homepage | URL equals `"https://www.saucedemo.com/"` |
| **Homepage URL** | `test_homepage_url_negative` | Verify homepage URL is not pointing to dashboard without login | URL does NOT equal `"https://www.saucedemo.com/inventory.html"` |
| **Dashboard URL** | `test_dashboard_url_positive` | Login with valid credentials (`standard_user`/`secret_sauce`) | Redirects to `"https://www.saucedemo.com/inventory.html"` & extracts content to `Webpage_task_11.txt` |
| **Dashboard URL** | `test_dashboard_url_negative` | Attempt login with invalid credentials (`invalid_user`/`wrong_password`) | Login fails with error message `"Epic sadface:"`, remains on homepage URL |

---

## ⚙️ Setup and Installation

1. **Clone the Repository**:
   ```bash
   git clone <your-repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure Chrome/Chromium Browser is Installed**:
   The script uses Selenium with Chrome in headless mode.

---

## 🚀 Execution Instructions

### 1. Run the Standalone Script
To execute the automation script directly and generate `Webpage_task_11.txt`:
```bash
python3 task10_saucedemo.py
```

### 2. Run the Pytest Test Suite & Generate HTML Report
To execute all test cases and generate the mandatory **HTML report**:
```bash
pytest --html=reports/report.html --self-contained-html -v
```

View the generated report by opening `reports/report.html` in any web browser.

---

## 📋 Compliance & Code Hygiene
- **PEP 8 Compliant**: Clean code formatting and proper indentations.
- **Detailed Docstrings & Comments**: Clear explanations for each function and test step.
- **Fixture Reusability**: Selenium driver management via `conftest.py` fixture.
- **Self-Contained Report**: HTML report includes metadata, test execution status, and pass/fail summary.

---

© 2026 GUVI Task Submission
