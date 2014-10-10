import os

from django.contrib.gis.geoip import GeoIP

from geodashboard.models import Visits

GEOFILES_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'db/')


class GeoMiddleware(object):
    def process_request(self, request):
        """
        Tries to catch the real IP of the request and adds geo details
        to the request itself. The value of request.GEO is a dictionary
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

        # Tries to get the value of x-forwarded-for header
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            # The first address **should** be the real one, others
            # are supposed to be proxied IPs.
            ip = x_forwarded_for.split(', ')[0]
        else:
            # If not x-forwarded-for is present, set the IP to
            # remote address, note that REMOTE_ADDR is not guaranteed to
            # be the real IP.
            ip = request.META.get('REMOTE_ADDR')

        # Settings cache to 1 opens the file the first time
        # middleware is used and puts it into memory to
        # speed up lookup during following requests.
        geoip = GeoIP(GEOFILES_DIR, cache=1)
        request.GEO = geoip.city(ip)
        save_request(request, ip)

    def process_response(self, request, response):
        return response


def save_request(request, ip):
    if isinstance(request.GEO, dict):
        data = {
            'ip': ip,
            'country': request.GEO.get('country_code'),
            'url': request.path,
            'referer': request.META.get('HTTP_REFERER') or '',
            'agent': request.META.get('HTTP_USER_AGENT') or ''
        }
        Visits.objects.create(**data)
