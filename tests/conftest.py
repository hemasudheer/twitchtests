import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def setup_mobile_emulator(device_name="Pixel 4"):
    chrome_options = Options()
    mobile_emulation = {"deviceName": device_name}
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(options=chrome_options)
    return driver


@pytest.fixture(scope="function")
def driver():
    driver = setup_mobile_emulator()
    yield driver
    driver.quit()


