from browser import Browser
from config import Config
import time
from general import General
from buildings import Buildings

class OgameBot(object):
    def __init__(self):
        # Instance of Config Util
        self.config = Config()
        # Instance of Browser Util
        self.browser = Browser(self.config)
        # AutoLogin when Init
        self.login()

    def overview(self):
        print(General(self.browser).get_resources())
        print(Buildings(self.browser).get_buildings_data())

    def build(self, id):
        Buildings(self.browser).build_structure(id)

    def login(self):
        # Open Login page
        self.browser.open_page('https://it.ogame.gameforge.com/')
        # Switch to login modal
        elem = self.browser.find_element_by('xpath', "//a[@href='#login']")
        self.browser.click(elem)
        # Fill Modal Form
        # Modal Email
        elem = self.browser.find_element_by('id', 'usernameLogin')
        self.browser.send_keys(elem, self.config.email)
        # Modal Password
        elem = self.browser.find_element_by('id', 'passwordLogin')
        self.browser.send_keys(elem, self.config.password)
        # Click Login Button
        elem = self.browser.find_element_by('id', 'loginSubmit')
        self.browser.click(elem)
        # Select the Universe
        time.sleep(2)
        elem = self.browser.find_element_by('xpath', "//div[@id='accountlist']/div[@class='ReactTable']/div[@class='rt-table']/div[@class='rt-tbody']/div[@class='rt-tr-group open']/div[@class='rt-tr -odd']/div[@class='rt-td action-cell']/button")
        self.browser.click(elem)
        self.browser.switch_tab(1)
        # And we are in

