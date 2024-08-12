import unittest
from flask import Flask, json
from app import app  # Assuming your Flask app is named app.py

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_fetch_data(self):
        response = self.app.get('/fetch-data')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 3)  # Expecting 3 items in mock_data
        self.assertIn("name", data[0]) 

    def test_process_data(self):
        mock_data = [
            {"id": 1, "name": "Product A", "price": 100},
            {"id": 2, "name": "Product B", "price": 150},
            {"id": 3, "name": "Product C", "price": 200}
        ]
        response = self.app.post('/process-data',
                                 data=json.dumps(mock_data),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"], "Data processed and stored successfully")

    def test_get_processed_data(self):

        mock_data = [
            {"id": 1, "name": "Product A", "price": 100},
            {"id": 2, "name": "Product B", "price": 150},
            {"id": 3, "name": "Product C", "price": 200}
        ]
        self.app.post('/process-data',
                      data=json.dumps(mock_data),
                      content_type='application/json')

        
        response = self.app.get('/get-processed-data')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 3)  
        self.assertEqual(data[0]["name"], "PRODUCT A")  # Check if the name is in uppercase

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
