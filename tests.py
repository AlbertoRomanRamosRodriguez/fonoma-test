import unittest
import requests
import json

class TestEndpoint(unittest.TestCase):

    def get_request_result(self, test_name:str) -> tuple:

        with open('test.json', 'r') as json_f:
            tests_data:dict = json.load(json_f)
        
        url = 'http://127.0.0.1:8000/solution'
        headers = {
            "Content-Type": "application/json"
        }
        data = tests_data[test_name]['params']
        response = requests.post(url, json=data, headers=headers)
        
        expected_result = float(tests_data[test_name]['expected_result'])
        result = round(float(response.text),2)
        
        return (result, expected_result)

    def test_completed(self):
        result, expected_result = self.get_request_result('test_completed')
        print(f"\tTesting {result} == {expected_result} - Filter and sum orders with 'completed' status")
        self.assertEqual(result, expected_result)
    
    def test_pending(self):
        result, expected_result = self.get_request_result('test_pending')
        print(f"\tTesting {result} == {expected_result} - Filter and sum orders with 'pending' status")
        self.assertEqual(result, expected_result)

    def test_invalid_status(self):
        result, expected_result = self.get_request_result('test_invalid_status')
        print(f"\tTesting {result} == {expected_result} - Inducing an invalid status")
        self.assertEqual(result, expected_result)
    
    def test_negative(self):
        result, expected_result = self.get_request_result('test_negative')
        print(f"\tTesting {result} == {expected_result} - Inducing negative values")
        self.assertEqual(result, expected_result)

    def test_invalid_criterion(self):
        result, expected_result = self.get_request_result('test_invalid_criterion')
        print(f"\tTesting {result} == {expected_result} - Inducing an invalid criterion")
        self.assertEqual(result, expected_result)

    def test_missing_criterion(self):
        result, expected_result = self.get_request_result('test_missing_criterion')
        print(f"\tTesting {result} == {expected_result} - Sending a void criterion")
        self.assertEqual(result, expected_result)
    
    def test_fonoma_case(self):
        result, expected_result = self.get_request_result('test_fonoma_case')
        print(f"\tTesting {result} == {expected_result} - Testing the actual fonoma case")
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    msg = "\tTesting [result] == [obtained result] - [test description]"
    print(msg)
    print('\t'+'-'*len(msg))
    unittest.main()