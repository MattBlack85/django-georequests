import json

from django.test import TestCase
from django.test.client import RequestFactory

from .views import geoip


class GeoIPBaseTest(TestCase):
    def test_google_request(self):
        request = RequestFactory(HTTP_X_FORWARDED_FOR='173.194.113.110').get('/api/v1/geoip')
        response = geoip(request)

        google_json = {
            "City": "Mountain View",
            "IP": "173.194.113.110",
            "Country Code": "US",
            "Proxy": "No",
            "Country": "United States",
            "Latitude": 37.4192008972168,
            "Longitude": -122.05740356445312,
        }

        self.assertEquals(google_json, json.loads(response.content.decode()))
