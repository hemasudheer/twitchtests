from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.streamer_page import StreamerPage


def test_twitch_search(driver):
    # Initialization of page objects
    home_page = HomePage(driver)
    search_page = SearchPage(driver)
    streamer_page = StreamerPage(driver)

    home_page.load_twitch_url()
    home_page.accept_cookies()
    home_page.click_search_icon()
    search_page.enter_search_term("StarCraft II")
    search_page.scroll_down(times=2)
    search_page.select_streamer()
    streamer_page.wait_for_page_load()
    home_page.take_screenshot("pic.png")
