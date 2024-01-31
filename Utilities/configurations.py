import configparser


# creating new class for parsing the properties.ini file into below function
def getConfig():
    config = configparser.ConfigParser()
    config.read('C:\\Users\\ragenwark\\PycharmProjects\\pythonProject1\\Utilities\\properties.ini')
    return config
