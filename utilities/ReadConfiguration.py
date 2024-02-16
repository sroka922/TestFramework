from configparser import ConfigParser


def read_configuration(category, key):
    config = ConfigParser()
    config.read("C:\\Users\\kryst\\PycharmProjects\\TestFramework\\configurations\\config.ini")
    return config.get(category, key)
