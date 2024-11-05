#!/usr/bin/env python3
"""Unittest module for utils module"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


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
