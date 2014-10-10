django-georequests
============

[![Build Status](https://travis-ci.org/MattBlack85/django-georequests.svg?branch=master)](https://travis-ci.org/MattBlack85/django-georequests)

### Dependencies
To use this app you need:
* GeoIP `sudo yum install GeoIP` or your packet manager if not on Fedora/RedHat/CentOS

### Installation
* Clone the repo
* `cd` to the repo
* run `python setup.py install`

### Use
This package is made of 3 components, a middleware, an additional url and a dashboard.
Below a description of every component and how you can use it.


### GeoMiddleware
This is a middleware you can add into your settings, to use it:
* Add the middleware to MIDDLEWARE_CLASSES variable in you settings, the geomiddleware does not require any special ordering, it can go first or last, or in the middle without difference.
  ```Python
  MIDDLEWARE_CLASSES = (
      'django.contrib.sessions.middleware.SessionMiddleware',
      .......,
      .......,
      'georequests.geomiddlewares.middleware.GeoMiddleware',
  )
  ```
* Add geodashboard to your installed apps:
  ```
  INSTALLED_APPS = (
      .....,
      .....,
      geodashboard,
  )
  ```

  After adding the middleware every incoming request will have a new attribute, GEO, which holds some geographical information regarding the request's IP e.g
  ```JSON
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
  ```
* You can use that information to have a better redirection if you use i18n, or to save those informations for later analysis. Every request is saved
  into the database, storing the requested url, the ip, the country, the agent and the referer.

### GeoIP
This exposes a uri like `/api/v1/geoip` into your app, you can then hit this uri to get some information regarding an IP. It returns a JSONResponse.

* Add georequests to your INSTALLED_APPS in your settings file:
  ```Python
  INSTALLED_APPS = (
      .....,
      .....,
      georequests,
  )
  ```

* edit your main <strong>urls.py</strong> adding the following line (you can change the uri in whatever you want):
  `url(r'^api/v1/geoip/$', include('reversegeoip.urls')),`
* Run your test server and surf to that URL.

### GeoDashboard
In progress.........

        
### Some words
* When using a mobile phone the city is often missing (country is good), I think this happens because
of the nature of mobile phone's IP.
* When running on your test server you will get `{"Message": "No data for that IP"}`, this happens because
LAN IPs like `192.168.0.1` are (of course!) not geolocalizable. This problem is persistent also when you
try to run your server behind a router, if your server runs behind a router every request passed by the router to your machine will have router's IP in the header giving incorrect results.
