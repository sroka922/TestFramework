import json
from abc import ABC, abstractmethod
import configurations


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


class FormUserData:

    def __init__(self, firstname, lastname, email, telephone, password, confirm):
        self.first_name = firstname
        self.last_name = lastname
        self.email = email
        self.telephone = telephone
        self.password = password
        self.confirm_password = confirm


class FormTestData(JsonTestData):
    path = "C:\\Users\\Krystian922\\PycharmProjects\\TestFramework\\configurations\\Form.json"

    def get_test_data(self, filename=path):
        with open(filename, 'r') as file:
            data = json.load(file)
        return [FormUserData(user['firstname'], user['lastname'], user['email'], user['telephone'],
                             user['password'], user['confirm']) for user in data['FormData']]


class TestDataFactory:
    @staticmethod
    def get_test_data(test_data_type):
        if test_data_type == 'login':
            return TestLoginData().get_test_data()
        elif test_data_type == 'form':
            form_test_date = FormTestData()
            return form_test_date.get_test_data()
        else:
            raise ValueError("Unknown Test Data type")
