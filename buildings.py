from enum import Enum
from bs4 import BeautifulSoup
from util import Item, ItemAction, UrlProvider
import time
import re

class BuildingItem(Item):
    """
    Used for handle building items
    """
    pass

BUILDINGS_DATA = {
    # Contains all the ref id with the right name
    "mm": BuildingItem(1, "Metal Mine"),
    "cm": BuildingItem(2, "Crystal Mine"),
    "ds": BuildingItem(3, "Deuterium Synthesizer"),
    "sp": BuildingItem(4, "Solar Plant"),
    "fr": BuildingItem(12, "Fusion Reactor"),
    "ms": BuildingItem(22, "Metal Storage"),
    "cs": BuildingItem(23, "Crystal Storage"),
    "dt": BuildingItem(24, "Deuterium Tank"),

    "1": BuildingItem(1, "Metal Mine"),
    "2": BuildingItem(2, "Crystal Mine"),
    "3": BuildingItem(3, "Deuterium Synthesizer"),
    "4": BuildingItem(4, "Solar Plant"),
    "12": BuildingItem(12, "Fusion Reactor"),
    "102": BuildingItem(22, "Metal Storage"),
    "23": BuildingItem(23, "Crystal Storage"),
    "24": BuildingItem(24, "Deuterium Tank")

}

class BuildingTypes(Enum):
    """
    1 Miner Metal
    2 Miner Crystal
    3 Miner Deuterium
    4 Power Plant
    5 Fusion
    """

    MetalMine = "1"
    CrystalMine = "2"
    DeuteriumSynthesizer = "3"
    SolarPlant = "4"
    FusionReactor = "12"
    SolarSatellite = "202"
    MetalStorage = "22"
    CrystalStorage = "23"
    DeuteriumTank = "24"


class BuildingData(object):
    """
    Data Extracted with scraping
    """
    def __init__(self, building, level):
        self.building = building
        self.level = level

class Buildings(object):

    def __init__(self, browser):
        # Instance of the browser
        self.browser = browser

    def get_buildings_data(self):
        print('Getting Buildings Data')
        # Scrap the page
        soup = BeautifulSoup(self.browser.page_source(), 'lxml')
        # Get all buttons with class
        building_buttons = soup(attrs={'class': "detail_button"})

        buildings = []
        for building_button in building_buttons:
            building_data = self.get_building_data_from_button(building_button)

            # Check if data is none
            if building_data is not None:
                # Add it to the array
                buildings.append(building_data)

        # Return all buildings data
        return buildings

    @staticmethod
    def get_building_data_from_button(building_button):
        """
        Read the building data from the building button
        :param building_button:
        :return: readed data
        """
        # Get ref from id
        building_id = building_button['ref']
        # Use the id for get the item name
        building_data = BUILDINGS_DATA.get(building_id)

        # If item is none this mean he's not available or under construction
        if building_data is not None:
            try:
                building_info = "".join(building_button.find("span", {"class": "level"}).findAll(text=True, recursive=False)[1])
            # Handle the exception by putting the item has last one
            except IndexError:
                building_info = "".join(building_button.find("span", {"class": "level"})
                                        .findAll(text=True, recursive=False)[0])
            level = int(re.sub("[^0-9]", "", building_info))
            # Return an item with all data
            return ItemAction(BuildingItem(building_data.id, building_data.name), level)
        else:
            # No data scrapped
            return None

    def build_structure(self, id):
        if self.is_in_construction_mode():
            print('Already building')
            return
        else:
            self.build_structure_item(id)

    def build_structure_item(self, building_id):

        # Get into resources page
        # Check if is already on resources page else redirect
        if (self.browser.current_url() != UrlProvider().get_page_url('resources')):
            self.browser.open_page(UrlProvider().get_page_url('resources'))

        # Open Mineral Modal
        elem = self.browser.find_element_by('xpath', (f"//a[@ref='{building_id}']"))
        self.browser.click(elem)
        time.sleep(2)
        # Submit Request
        # We use this method because they generate random token
        elem = self.browser.find_element_by('xpath', "//a[@class='build-it']")
        self.browser.click(elem)

    def is_in_construction_mode(self):
        soup = BeautifulSoup(self.browser.page_source(), 'lxml')

        return soup.find("div", {"class": "construction"}) is not None