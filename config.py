from configparser import ConfigParser
import os
import re

class Config(object):
    def __init__(self):
        config = ConfigParser()

        # Read config file
        config_file = config.read('user.cfg')

        if not config_file:
            print('Missing config file')

            exit()
        else:
            # Prepare to grab configuration from the file

            # UserConfig Options
            self.email = config.get('UserInfo', 'Email')
            self.password = config.get('UserInfo', 'Password')
            self.universe = config.get('UserInfo', 'Universe')
            self.country = config.get('UserInfo', 'Country')