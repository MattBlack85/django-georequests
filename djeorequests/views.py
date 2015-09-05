import os

from django.contrib.gis.geoip import GeoIP
try:
    from django.http import JsonResponse
except ImportError:
    import json
    from django.http import HttpResponse

DB_PATH = os.path.dirname(__file__)


def geoip(request):
    # Try to get the IP from HTTP_X_FORWARDED_FOR
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    behind_proxy = "Can't be established"
    geoip = GeoIP(os.path.join(DB_PATH, 'db/'))
    data = {'message': 'No data for your ip'}
    no_data = 'No data'

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # Get the first IP of the list, the real one.
        behind_proxy = 'Yes' if len(x_forwarded_for.split(',')) > 1 else 'No'
    else:
        # Set the ip to the remote address if we have no x_forwarded_for in the request
        ip = request.META.get('REMOTE_ADDR')

    geo_data = geoip.city(ip)
    if geo_data:
        country = geo_data['country_name']
        country_code = geo_data['country_code']
        city = geo_data['city']
        lat = geo_data['latitude']
        lon = geo_data['longitude']
        data = {
            'IP': ip,
            'Proxy': behind_proxy,
            'Country': country if country else no_data,
            'Country Code': country_code if country_code else no_data,
            'City': city if city else no_data,
            'Latitude': lat if lat else no_data,
            'Longitude': lon if lon else no_data,
        }

    try:
        return JsonResponse(data)
    except NameError:
        return HttpResponse(json.dumps(data), content_type='application/json')
