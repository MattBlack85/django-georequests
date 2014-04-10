from django.db import models
import jsonfield


class users(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    location = jsonfield.JSONField()
