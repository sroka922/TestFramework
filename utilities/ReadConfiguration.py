from configparser import ConfigParser

FILEPATH = "C:\\Users\\Krystian922\\PycharmProjects\\TestFramework\\configurations\\config.ini"


def read_configuration(category, key):
    config = ConfigParser()
    config.read(FILEPATH)
    return config.get(category, key)
