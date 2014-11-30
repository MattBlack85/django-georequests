from django.db import models


class Visit(models.Model):
    ip = models.GenericIPAddressField()
    country = models.CharField(max_length=25, blank=True, default='')
    url = models.CharField('requested url', max_length=100)
    referer = models.CharField(max_length=100, blank=True, default='')
    agent = models.CharField(max_length=100)
