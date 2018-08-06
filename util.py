
class UrlProvider():
    """
    Contains All the usefull links for navigate trough the browser
    """
    def __init__(self):
        self.main_url = 'https://s154-it.ogame.gameforge.com/game/index.php'
        # All the pages of the browser
        self.pages = {
            'overview': self.main_url + '?page=overview',
            'resources': self.main_url + '?page=resources',
            'research': self.main_url + '?page=research',
            'shipyard': self.main_url + '?page=shipyard',
            'defense': self.main_url + '?page=defense',
            'fleet': self.main_url + '?page=fleet1',
            'galaxy': self.main_url + '?page=galaxy',
            'galaxyContent': self.main_url + '?page=galaxyContent&ajax=1',
            'messages': self.main_url + '?page=messages',
            'movement': self.main_url + '?page=movement',
            'missileAttack': self.main_url + '?page=missileattacklayer',
            'eventList': self.main_url + '?page=eventList&ajax=1'
        }

    def get_pages(self) -> object:
        """
        :return: List of pages
        """

        return self.pages

    def get_page_url(self, page) -> str:
        """
        :param page: Page to navigate
        :return: Url of the page
        """

        url = self.pages.get(page)
        return url

    def get_main_url(self):
        """
        :return: Main Url
        """

        return self.main_url

class Resources(object):
    """
    Object to abstract an Resource in game
    """
    def __init__(self, metal, crystal, deuterium, energy, dark_matter):
        self.metal = metal
        self.crystal = crystal
        self.deuterium = deuterium
        self.energy = energy
        self.dark_matter = dark_matter

    def __str__(self):
        """
        :return: A Formated String of the Resources
        """
        result = []
        result.append(f'Metal: {self.metal}')
        result.append(f'Crystal: {self.crystal}')
        result.append(f'Deuterium: {self.deuterium}')
        result.append(f'Energy: {self.energy}')
        result.append(f'Dark Matter: {self.dark_matter}')

        return ', '.join(result)

class Item(object):
    """
    Abstraction of an Item in game
    """
    def __init__(self, id, name):
        self.name = name
        self.id = id

    def __str__(self):
        return (f'Description {self.name}, Id: {self.id}')

class ItemAction(object):
    """
    Abstraction of an clickable item
    """
    def __init__(self, item, amount):
        self.item = item
        self.amount = amount

    def __str__(self):
        return (f'Description {self.item.name}, Id: {self.item.id}, Amount: {self.amount}')