import os

from django.contrib.gis.geoip import GeoIP

GEOFILES_DIR = os.path.dirname(__file__)


class GeoMiddleware(object):
    def process_request(self, request):
        """
        Tries to catch the real IP of the request and adds geo details
        to the request itself. The value of request.GEODATA is a dictionary
        that looks like:

        {
            'area_code': 650,
            'charset': 0,
            'city': u'Mountain View',
            'continent_code': u'NA',
            'country_code': u'US',
            'country_code3': u'USA',
            'country_name': u'United States',
            'dma_code': 807,
            'latitude': 37.4192008972168,
            'longitude': -122.05740356445312,
            'postal_code': u'94043',
            'region': u'CA'
        }
        """

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(', ')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        # Settings cacheto 1 opens the file the first time
        # the middleware is used and puts it into memory to
        # speed up lookup during the following requests.
        geoip = GeoIP(GEOFILES_DIR, cache=1)
        geodata = GeoData(geoip.city(ip))
        request.GEODATA = geodata.data

    def process_response(self, request, response):
        return response


class GeoData(object):
    def __init__(self, data):
        self.data = data
