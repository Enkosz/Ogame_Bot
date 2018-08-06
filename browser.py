from selenium import webdriver
from selenium.webdriver.remote import webelement
from config import Config

class Browser(object):
    def __init__(self, config: Config):
        # Navigation Info
        self.login_url = 'https://it.ogame.gameforge.com/'
        self.index_url = 'https://s154-it.ogame.gameforge.com/game/index.php?page=overview'

        # UserInfo
        self.email = config.email
        self.password = config.password
        self.universe = config.universe
        self.country = config.country

        # Instance of browser
        self.browser = webdriver.Chrome('C:\chromedriver.exe')

    def open_page(self, page: str) -> None:
        self.browser.get(page)

    def find_element_by(self, mode: str, query: str) -> webelement:
        if (mode == 'xpath'):
            return self.browser.find_element_by_xpath(query)
        elif (mode == 'id'):
            return self.browser.find_element_by_id(query)
        else:
            return self.browser.find_element_by_id(query)

    def send_keys(self, element: webelement, keys: str) -> None:
        element.send_keys(keys)

    def click(self, element: webelement) -> None:
        element.click()

    def switch_tab(self, index: int) -> None:
        self.browser.switch_to_window(self.browser.window_handles[index])

    def current_url(self) -> str:
        return self.browser.current_url

    def page_source(self):
        return self.browser.page_source