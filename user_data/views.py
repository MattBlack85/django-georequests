from django.shortcuts import render
from django.http import StreamingHttpResponse, HttpResponse
from django.contrib.gis.geoip import GeoIP
import json


def index(request):
    x_forwarded_for = request.META.get('REMOTE_ADDR')
    #print request.META
    behind_proxy = "You are behind a proxy" if len(x_forwarded_for.split(',')) > 1 else None

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    geoip = GeoIP('~/')

    geo_data = geoip.city(ip)
    
    if geo_data:
        country = geo_data.get('country_name')
        country_code = geo_data.get('country_code')
        city = geo_data.get('city')
        latitude = geo_data.get('latitude')
        longitude = geo_data.get('longitude')

        data = {"status_code": 200,
                "IP": ip,
                "Proxy": behind_proxy,
                "Country": country,
                "Country Code": country_code,
                "City": geo_data['city'] if geo_data['city'] else None,
                "Latitude": geo_data['latitude'] if geo_data['latitude'] else None,
                "Longitude": geo_data['longitude'] if geo_data['longitude'] else None}

    else:
        data = {"status_code": 200,
                "message": "No data for ip"}

    return StreamingHttpResponse(json.dumps(data), content_type="application/json")
