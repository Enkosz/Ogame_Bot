from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem
from bot import OgameBot

print('Starting bot')
# Instance of Bot
bot = OgameBot()


# Create console menu
menu = ConsoleMenu('OgameBot','An Ogame Automatizer')

# Options for menu item
overview_function = FunctionItem('Overview', bot.overview)
build_function = FunctionItem('Build', bot.build)


# Add Options to the menu
menu.append_item(overview_function)
menu.append_item(build_function)

# Shows menu
menu.show()

