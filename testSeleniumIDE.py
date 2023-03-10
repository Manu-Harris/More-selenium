import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestDefaultSuite():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_job(self):
    # Test name: job
    # Step # | name | target | value
    # 1 | open | https://www.seek.co.nz/ | 
    self.driver.get("https://www.seek.co.nz/")
    # 2 | setWindowSize | 855x599 | 
    self.driver.set_window_size(855, 599)
    # 3 | click | id=keywords-input | 
    self.driver.find_element(By.ID, "keywords-input").click()
    # 4 | type | id=keywords-input | python developer
    self.driver.find_element(By.ID, "keywords-input").send_keys("python developer")
    # 5 | click | css=.\_14uh99416 | 
    self.driver.find_element(By.CSS_SELECTOR, ".\\_14uh99416").click()
    # 6 | click | css=.yvsb870:nth-child(2) > .yvsb870:nth-child(1) > div:nth-child(1) > div:nth-child(1) > .yvsb870:nth-child(1) > .yvsb870:nth-child(2) > div:nth-child(1) > .yvsb870:nth-child(1) > .yvsb870:nth-child(2) > .yvsb870:nth-child(1) | 
    self.driver.find_element(By.CSS_SELECTOR, ".yvsb870:nth-child(2) > .yvsb870:nth-child(1) > div:nth-child(1) > div:nth-child(1) > .yvsb870:nth-child(1) > .yvsb870:nth-child(2) > div:nth-child(1) > .yvsb870:nth-child(1) > .yvsb870:nth-child(2) > .yvsb870:nth-child(1)").click()
    # 7 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 8 | click | css=.yvsb870:nth-child(1) > .yvsb870:nth-child(1) > div:nth-child(1) > .yvsb870:nth-child(1) > .yvsb870:nth-child(1) > .yvsb870:nth-child(1) > .yvsb870:nth-child(1) > .yvsb870:nth-child(1) > .yvsb870:nth-child(1) > .yvsb870:nth-child(1) > .yvsb870:nth-child(1) > .yvsb870:nth-child(1) > .yvsb870:nth-child(2) > .yvsb870:nth-child(1) > .yvsb870:nth-child(1) > .yvsb870:nth-child(1) > .yvsb870:nth-child(1) > .yvsb870:nth-child(1) | 
    self.driver.find_element(By.CSS_SELECTOR, ".yvsb870:nth-child(1) > .yvsb870:nth-child(1) > div:nth-child(1) > .yvsb870:nth-child(1) > .yvsb870:nth-child(1) > .yvsb870:nth-child(1) > .yvsb870:nth-child(1) > .yvsb870:nth-child(1) > .yvsb870:nth-child(1) > .yvsb870:nth-child(1) > .yvsb870:nth-child(1) > .yvsb870:nth-child(1) > .yvsb870:nth-child(2) > .yvsb870:nth-child(1) > .yvsb870:nth-child(1) > .yvsb870:nth-child(1) > .yvsb870:nth-child(1) > .yvsb870:nth-child(1)").click()
    # 9 | click | css=.\_12ytqjg0:nth-child(1) > .\_1kzqo4e20 | 
    self.driver.find_element(By.CSS_SELECTOR, ".\\_12ytqjg0:nth-child(1) > .\\_1kzqo4e20").click()
  
