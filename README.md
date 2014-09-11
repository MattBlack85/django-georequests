django-reverseGeoIP
============

[![Build Status](https://travis-ci.org/MattBlack85/django-georequests.svg?branch=master)](https://travis-ci.org/MattBlack85/django-georequests)

### Dependencies
To use this app you will need:
* GeoIP `sudo yum install GeoIP`

### Installation
* Downlaod the repo
* `cd` to the repo
* `pip install dist/django-reversegeoip-0.1.tar.gzip`
* Now you have the app installed, add it to your INSTALLED_APPS in your settings file <br>
  <code>INSTALLED_APPS = (....., <br />
                          reversegeoip, <br />
                          .........., <br />
                      ) </code>

* edit your main <strong>urls.py</strong> adding the following line <br>
  `url(r'^api/v1/ReverseGeoIP/', include('reversegeoip.urls')),`
* Run your test server and surf to that URL.


### Scope
This is a simple django pluggable app to geolocalize an IP.
Given an IP e.g `72.14.207.99` it returns following JSON:

data = {"IP": 72.14.207.99,                `Address IP` <br />
        "Proxy": "No",                     `If user is behind a proxy or not (to test)` <br />
        "Country": "United States",        `country` <br />
        "Country Code": "USA",             `Country ISO-code` <br />
        "City": "Mountain View",           `city` <br />
        "Latitude": 37.4192008972168,      `latitude` <br />
        "Longitude": -122.05740356445312,  `longitude` <br />
        "Message": "Ok"                    `Confirmation that everything went ok` <br />
        }
        
### Some words
* When using a mobile phone the city is often missing (country is good), I think this happens because
of the nature of mobile phone's IP.
* When running on your test server you will get `{"Message": "No data for that IP"}`, this happens because
LAN IPs like `192.168.0.1` are (of course!) not geolocalizable. This problem is persistent also when you
try to run your server behind a router, if your server runs behind a router every request passed by the router to your machine will have router's IP in the header giving incorrect results.
