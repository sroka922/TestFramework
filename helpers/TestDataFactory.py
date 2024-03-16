from helpers.JsonTestData import TestLoginData, FormTestData


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
