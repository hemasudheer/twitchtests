from pages.base_page import BasePage
from selenium.webdriver.common.by import By

search_icon_locator = (By.XPATH, "//button[contains(@aria-label, 'Search')]")


class HomePage(BasePage):

    def click_search_icon(self):
        search_icon = self.wait_for_element_clickable(search_icon_locator)
        search_icon.click()

    def load_twitch_url(self):
        self.driver.get("https://www.twitch.tv")

    def accept_cookies(self):
        try:
            # Define the locator for the "Accept" button
            accept_button_locator = (By.XPATH, "//div[contains(text(),'Accept')]")
            import pdb;pdb.set_trace()


            accept_button_locator = (By.XPATH, "//div[contains(text(),'Accept')]")

            accept_button = self.wait_for_element_clickable(accept_button_locator)

            # Click the "Accept" button
            accept_button.click()
            print("Clicked the 'Accept' button.")
        except Exception as e:
            # If the "Accept" button is not present or clickable, ignore the exception
            print(f"'Accept' button not present or not clickable: {e}")
