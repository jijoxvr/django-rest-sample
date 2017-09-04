from __future__ import unicode_literals

from django.db import models

class Vendor(models.Model):
    name = models.TextField(max_length=50)
    service_type = models.TextField(max_length=50)
    since = models.DateField()
    currency = models.TextField()
    is_active = models.BooleanField()

# Create your models here.
