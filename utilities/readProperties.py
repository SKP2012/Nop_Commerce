import configparser  # Importing configparser to read .ini files

config = configparser.RawConfigParser()  # Create an instance of RawConfigParser to read the configuration file
# Using rawConfigParser to read properties without interpolation.
# Create variable config to hold the configparser object, rawConfigParser is a class.
config.read(".\\Configurations\\config.ini")  # Read the config.ini file from the Configurations directory using location
# Create a class here
class ReadConfig:
     @staticmethod
     def getApplicationURL():
         url = config.get('Common info', 'baseURL')  # Get the base URL from the config file
         return url
     @staticmethod
     def getUserEmail():
         username = config.get('Common info', 'useremail')  # Get the user email from the config file
         return username
     @staticmethod
     def getPassword():
         password = config.get('Common info','password') # Get the password from the config file
         return password






