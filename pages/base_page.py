from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time
import os
from datetime import datetime

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def scroll_down(self, times=2):
        actions = ActionChains(self.driver)
        for _ in range(times):
            actions.send_keys(Keys.PAGE_DOWN).perform()
            time.sleep(2)

    def wait_for_element(self, locator, wait_time=10):
        WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located(locator)
        )
        time.sleep(5)

    def wait_for_element_clickable(self, locator, wait_time=10):
        elem = WebDriverWait(self.driver, wait_time).until(
            EC.element_to_be_clickable(locator)
        )
        time.sleep(5)
        return elem

    def take_screenshot(self, filename):
        screenshots_dir = os.path.join(os.getcwd(), "screenshots")
        time_stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        new_file_name = f"{time_stamp}_{filename}"
        file_path = os.path.join(screenshots_dir, new_file_name)
        self.driver.save_screenshot(file_path)