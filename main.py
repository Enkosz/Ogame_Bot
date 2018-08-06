from consolemenu import ConsoleMenu, SelectionMenu
from consolemenu.items import FunctionItem, SubmenuItem
from bot import OgameBot

print('Starting bot')
# Instance of Bot
bot = OgameBot()


# MAIN MENU CONSOLE
mainMenu = ConsoleMenu('OgameBot','An Ogame Automatizer')

# BUILD MENU SECTION
buildMenu = ConsoleMenu('Building Menu')
buildMenu_Mining = ConsoleMenu('Mining Menu')
buildMenu_Structure = ConsoleMenu('Structure Menu')
buildMenu_Defense = ConsoleMenu('Defense Menu')
buildMenu_Fleet = ConsoleMenu('Fleet Menu')

# FUNCTIONS TO EACH MENU
buildMenuMining_FunctionMetal = FunctionItem('Metal Mine', bot.build, args='1')
buildMenuMining_FunctionCrystal = FunctionItem('Crystal Mine', bot.build, args='2')
buildMenuMining_FunctionDeuterium = FunctionItem('Deuterium Mine', bot.build, args='3')
buildMenuMining_FunctionEnergy = FunctionItem('Enery Plant', bot.build, args='4')

# ADD TO EACH MENU
buildMenu_Mining.append_item(buildMenuMining_FunctionMetal)
buildMenu_Mining.append_item(buildMenuMining_FunctionCrystal)
buildMenu_Mining.append_item(buildMenuMining_FunctionDeuterium)
buildMenu_Mining.append_item(buildMenuMining_FunctionEnergy)

# SUBMENUS BUILDING
subMenuMining = SubmenuItem('Mining Menu', buildMenu_Mining, buildMenu)
subMenuStructure = SubmenuItem('Structure Menu', buildMenu)
subMenuDefense = SubmenuItem('Defense Menu', buildMenu)
subMenuFleet = SubmenuItem('Fleet Menu', buildMenu)
buildSubMenu = SubmenuItem('Building Menu', buildMenu)

# SUBMENUS APPENDING TO MAIN MENU
buildMenu.append_item(subMenuMining)
buildMenu.append_item(subMenuStructure)
buildMenu.append_item(subMenuDefense)
buildMenu.append_item(subMenuFleet)

# Add Options to the menu
mainMenu.append_item(buildSubMenu)

# Shows menu
mainMenu.show()


