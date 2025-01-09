from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

search_input_locator = (By.XPATH, "//input[@type='search']")
streamer_locator = (By.XPATH, "//a[contains(@href, '/videos/')]")


class SearchPage(BasePage):

    def enter_search_term(self, term):
        search_input = self.wait_for_element(search_input_locator)
        search_input.send_keys(term)
        search_input.send_keys(Keys.ENTER)

    def select_streamer(self):
        streamer = self.wait_for_element_clickable(streamer_locator)
        streamer.click()