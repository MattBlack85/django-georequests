from django.conf.urls import patterns, include, url

from reversegeoip import views

urlpatterns = patterns('',
        url(r'^$', views.reverseGeoIP),
)
