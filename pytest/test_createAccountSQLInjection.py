# Generated by Selenium IDE
import pytest
import time
import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from dotenv import load_dotenv
load_dotenv()

class TestCreateAccountSQLInjection():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_createAccountSQLInjection(self):
    base_url = os.environ.get('TEST_HOST', 'default_url_if_not_set')
    self.driver.get("https://" + base_url + "/users/create_account.php")
    self.driver.find_element(By.ID, "first_name").send_keys("\' OR 1=1; -- ")
    self.driver.find_element(By.ID, "last_name").send_keys("Last_name")
    self.driver.find_element(By.ID, "email").send_keys("email@email.com")
    self.driver.find_element(By.ID, "username").send_keys("usernameasd")
    self.driver.find_element(By.ID, "password").send_keys("password")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    value = self.driver.find_element(By.CSS_SELECTOR, "b:nth-child(4)").get_attribute("value")
    assert value != "Fatal error"
  