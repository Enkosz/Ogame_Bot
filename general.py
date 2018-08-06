from util import UrlProvider, Resources
from browser import Browser
from bs4 import BeautifulSoup

class General():
    """
    This class is used for general actions
    """
    def __init__(self, browser: Browser):
        # Get Instance of browser
        self.browser = browser

    def get_resources(self):
        """
        :return: All Resources Avaialable
        """
        print('Getting resources')
        # Redirect Browser to resources page
        self.browser.open_page(UrlProvider().get_page_url('resources'))
        # Scrap the page
        soup = BeautifulSoup(self.browser.page_source(), 'lxml')

        # Get Resources with Scraping as Intager
        metal = int(soup.find(id='resources_metal').text.replace('.', ''))
        crystal = int(soup.find(id='resources_crystal').text.replace('.', ''))
        deuterium = int(soup.find(id='resources_deuterium').text.replace('.', ''))
        energy = int(soup.find(id='resources_energy').text.replace('.', ''))
        dark_matter = int(soup.find(id='resources_darkmatter').text.replace('.', ''))

        # Return Resource Object with all value
        return (Resources(metal, crystal, deuterium, energy, dark_matter)).__str__()