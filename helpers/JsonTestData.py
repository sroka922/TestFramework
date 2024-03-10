import json
from abc import ABC, abstractmethod
from json import JSONDecodeError

import os

import configurations
from helpers.FormUserData import FormUserData


class JsonTestData(ABC):

    @abstractmethod
    def get_test_data(self):
        raise NotImplementedError


class TestLoginData(JsonTestData):
    path = os.path.join(os.path.dirname(__file__), '..', 'configurations', 'Credentials.json')

    def get_test_data(self, filename=path):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            print(f"File{self.path} not found")
            return None
        except JSONDecodeError:
            print(f"Decode Error")
            return None
        return [(user['email'], user['password']) for user in data['Credentials']]


class FormTestData(JsonTestData):
    path = os.path.join(os.path.dirname(__file__), '..', 'configurations', 'Form.json')

    def get_test_data(self, filename=path):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            print(f"File{self.path} not found")
            return None
        except JSONDecodeError:
            print(f"JSON Error")
            return None
        return [FormUserData(user['firstname'], user['lastname'], user['email'], user['telephone'],
                             user['password'], user['confirm']) for user in data['FormData']]
