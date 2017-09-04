from django.contrib import admin
from .models import Bill
from vendor.models import Vendor

admin.site.register(Bill)
admin.site.register(Vendor)

# Register your models here.
