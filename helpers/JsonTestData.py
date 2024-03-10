import json
from abc import ABC, abstractmethod
import configurations
from helpers.FormUserData import FormUserData


class JsonTestData(ABC):

    @abstractmethod
    def get_test_data(self):
        raise NotImplementedError


class TestLoginData(JsonTestData):
    path = "C:\\Users\\Krystian922\\PycharmProjects\\TestFramework\\configurations\\Credentials.json"

    def get_test_data(self, filename=path):
        with open(filename, 'r') as file:
            data = json.load(file)
        return [(user['email'], user['password']) for user in data['Credentials']]


class FormTestData(JsonTestData):
    path = "C:\\Users\\Krystian922\\PycharmProjects\\TestFramework\\configurations\\Form.json"

    def get_test_data(self, filename=path):
        with open(filename, 'r') as file:
            data = json.load(file)
        return [FormUserData(user['firstname'], user['lastname'], user['email'], user['telephone'],
                             user['password'], user['confirm']) for user in data['FormData']]


