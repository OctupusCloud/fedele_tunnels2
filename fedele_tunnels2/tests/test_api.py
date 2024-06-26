#!/usr/bin/env python

"""Tests for `fedele_tunnels2` package."""
from django.urls import reverse
from fedele_tunnels2.tests.custom import APITestCase


class AppTest(APITestCase):
    """
    Test the availability of the NetBox Tunnels API root
    """

    def test_root(self):
        url = reverse("plugins-api:fedele_tunnels2-api:api-root")
        response = self.client.get(f"{url}?format=api", **self.header)

        self.assertEqual(response.status_code, 200)