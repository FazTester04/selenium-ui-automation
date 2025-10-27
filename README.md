# Selenium Web UI Automation

This project showcases **automated web UI testing** using **Selenium WebDriver** and **Python**.  
It simulates real user interactions — such as clicking buttons, typing in fields, and verifying page behavior — to ensure the front-end of a web application works as expected.

---

## 🚀 Features
-  Automates browser actions (open pages, click, type, submit)
-  Validates UI elements and user flows
-  Supports **Chrome**, **Firefox**, and **Edge**
-  Runs locally or in CI/CD pipelines
-  Generates readable test results using `pytest`

---

## 🧱 Project Structure
```
selenium-ui-automation/
├── tests/
│   └── test_google_search.py      # Sample test case
├── drivers/                       # Folder for WebDrivers (e.g., chromedriver.exe)
├── requirements.txt               # Dependencies
└── README.md                      # Documentation
```

---

##  Tools & Libraries
| Tool | Purpose |
|------|----------|
| **Python 3** | Main programming language |
| **Selenium WebDriver** | Automates browser interactions |
| **pytest** | Test runner and report generator |
| **ChromeDriver** | Bridge between Selenium and Chrome browser |

---

##  Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/FazTester04/selenium-ui-testing.git
cd selenium-ui-testing
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Download and Setup ChromeDriver
- Check your Chrome version:  
  Open Chrome → go to `chrome://settings/help`
- Download the matching [ChromeDriver](https://chromedriver.chromium.org/downloads)
- Place it in the `drivers/` folder  
- Add it to your system PATH if needed
 

---

##  Example Output

```
============================= test session starts =============================
collected 1 item

tests/test_google_search.py::test_google_search PASSED                  [100%]

============================== 1 passed in 5.21s ==============================
```

---

##  What This Project Demonstrates
- Browser automation fundamentals (locators, waits, assertions)
- Web UI validation 
- Test organization and reporting using `pytest`
- Cross-browser setup via WebDrivers

---

##  Next Steps (Future Improvements)
- Add Page Object Model (POM) structure
- Integrate with Jenkins CI/CD
- Run tests in Dockerized containers
- Generate HTML reports with `pytest-html`

---

 **Author:** Fazni Alif Asyraf  
 **Role:** Software QA Engineer  
 **Focus:** Automated UI Testing, CI/CD Integration, and Scalable QA Frameworks
