"""
Test Cases for Counter Web Service
"""
from unittest import TestCase
import status
from counter import app

class CounterTest(TestCase):
    """Test Cases for Counter Web Service"""

    def setUp(self):
        self.client = app.test_client()

    def test_create_a_counter(self):
        """It should create a counter"""
        result = self.client.post("/counters/foo")
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        data = result.get_json()
        self.assertIn("foo", data)
        self.assertEqual(data["foo"], 0)

    def test_duplicate_counter(self):
        """It should return an error for duplicates"""
        result = self.client.post("/counters/bar")
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        result = self.client.post("/counters/bar")
        self.assertEqual(result.status_code, status.HTTP_409_CONFLICT)

    def test_update_a_counter(self):
        """It should update/increment the counter"""
        result = self.client.post("/counters/baz")
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        data = result.get_json()
        baseline = data["baz"]
        #Update the counter
        result = self.client.put("/counters/baz")
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        data = result.get_json()
        self.assertEqual(data["baz"], baseline + 1)

    def test_read_a_counter(self):
        """It should read the current state of counter"""
        # Create the new counter
        result = self.client.post("/counters/bin")
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        # Read the counter
        result = self.client.get("/counters/bin")
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        data = result.get_json()
        self.assertEqual(data["bin"], 0)

    def test_delete_a_counter(self):
        """It should delete a counter"""
        # Create a new counter
        result = self.client.post("/counters/fob")
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)

        # Delete the counter
        result = self.client.delete("/counters/fob")
        self.assertEqual(result.status_code, status.HTTP_204_NO_CONTENT)
        