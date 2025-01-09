from pages.base_page import BasePage
from selenium.webdriver.common.by import By

video_locator = (By.XPATH, "//video")


class StreamerPage(BasePage):

    def wait_for_page_load(self):
        self.wait_for_element(video_locator)
