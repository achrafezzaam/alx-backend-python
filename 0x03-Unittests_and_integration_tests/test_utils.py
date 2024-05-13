#!/usr/bin/env python3
''' Test file for the utils methods '''
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import Dict, Tuple, Union


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
                self,
                nested_map: Dict,
                path: Tuple[str],
                val: Union[Dict, int]
            ) -> None:
        self.assertEqual(access_nested_map(nested_map, path), val)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(
                self,
                nested_map: Dict,
                path: Tuple[str]
            ) -> None:
        self.assertRaises(KeyError)


class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url: str, payload: Dict) -> None:
        params = {"json.return_value": payload}
        with patch("requests.get", return_value=Mock(**params)) as get_req:
            self.assertEqual(get_json(url), payload)
            get_req.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    def test_memoize(self) -> None:
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(
                    TestClass,
                    "a_method",
                    return_value=lambda: 42,
                ) as mem_fn:
            test_obj = TestClass()
            self.assertEqual(test_obj.a_property(), 42)
            self.assertEqual(test_obj.a_property(), 42)
            mem_fn.assert_called_once()
