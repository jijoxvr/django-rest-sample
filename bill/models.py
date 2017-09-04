from __future__ import unicode_literals

from django.db import models
from vendor.models import Vendor


class Bill(models.Model):
    vendor = models.ForeignKey(Vendor)
    amount = models.FloatField()
    bill_date = models.DateField()
    due_date = models.DateField()

# Create your models here.
