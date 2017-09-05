from __future__ import unicode_literals

from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=50)
    service_type = models.CharField(max_length=50)
    since = models.DateField()
    currency = models.CharField(max_length=10)
    is_active = models.BooleanField()

    def __unicode__(self):
        return '%s' % (self.name)

# Create your models here.
