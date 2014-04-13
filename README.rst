=====
ReverseGeoIP
=====

This modules allows to gather some informations regarding the IP which made
the request. Basically you can obtain city, country, isocode, latitude
and longitude of associated with that IP. The associated view returns
data in JSON.

The reverse-search is known to not work well for mobile phones for
obvious reasons.


Quick start
-----------

1. Add "reverse-geo-ip" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'reverse-geo-ip',
    )

2. Include the polls URLconf in your project urls.py like this::

    url(r'^api/v1/ReverseGeoIP', include('reverse-geo-ip.urls')),

3. No need of model.

4. Start the development server and visit 
   http://127.0.0.1:8000/api/v1/ReverseGeoIP
   to see some data. Actually you will see "No data from this IP", this
   happens because home IPs like 192.168.0.134 can't be geolocalized
   (of course!). You should run this app not behind a router or
   similar because traffic filtrated by router has modified headers
   with router IP instead IP from original request. Also use NGINX
   or something like that to have HTTP_X_FORWARDED_FOR header
   in your request (useful to check if the user is behind a proxy).
