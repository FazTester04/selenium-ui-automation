from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

URL = "https://www.saucedemo.com/"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(URL)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_valid_login(driver):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    assert "inventory" in driver.current_url

def test_invalid_login(driver):
    driver.find_element(By.ID, "user-name").send_keys("wrong_user")
    driver.find_element(By.ID, "password").send_keys("wrong_pass")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(1)
    error = driver.find_element(By.XPATH, "//h3[@data-test='error']")
    assert "Epic sadface" in error.text
