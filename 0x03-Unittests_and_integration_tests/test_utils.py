#!/usr/bin/env python3
"""Unittest module for utils module"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map
from utils import get_json
from utils import memoize


class TestAccessNestedMap(unittest.TestCase):
    """A class that tests the access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test for the function to returns the expected output."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, missing_key):
        """Test for the function to raises a KeyError for invalid keys"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        # Check if the missing key is in the exception message
        self.assertEqual(str(context.exception), f"'{missing_key}'")


class TestGetJson(unittest.TestCase):
    """A class that tests the get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """Test for the function to returns the expected output"""
        with patch("utils.requests.get") as mock_get:
            # Create a Mock response object with a .json() method
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            # Call get_json and check its return value
            result = get_json(test_url)
            self.assertEqual(result, test_payload)

            # Check that requests.get was called once with test_url
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """A class that tests the memoize function."""

    def test_memoize(self):
        """Test that the function returns the expected output."""

        class TestClass:
            """A test class."""

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        # Create an instance of TestClass
        test_instance = TestClass()

        # Patch a_method to monitor its call count
        with patch.object(
                TestClass, 'a_method', return_value=42) as mock_method:
            # Call a_property twice
            result1 = test_instance.a_property
            result2 = test_instance.a_property

            # Check that both calls return the correct result
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            # Ensure a_method was only called once due to memoization
            mock_method.assert_called_once()
