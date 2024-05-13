#!/usr/bin/env python3
''' Test the client file '''
from client import GithubOrgClient
import unittest
from unittest.mock import MagicMock, Mock, patch, PropertyMock
from typing import Dict
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    ''' Test the GithubOrgClient class '''
    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"})
    ])
    @patch("client.get_json")
    def test_org(
            self,
            org: str,
            res: Dict,
            fn: MagicMock
            ) -> None:
        ''' Test the org method '''
        fn.return_value = MagicMock(return_value=res)
        client = GithubOrgClient(org)
        self.assertEqual(client.org(), res)
        fn.asser_called_once_with(
                "https://api.github.com/orgs/{org}"
                .format(org=org)
                )

    def test_public_repos_url(self) -> None:
        """Tests the _public_repos_ur method"""
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock,
                ) as org_mock:
            org_mock.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )
