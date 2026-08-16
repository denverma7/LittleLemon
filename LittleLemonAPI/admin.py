
from django.contrib import admin

from .models import Booking, Menu, MenuItem

# Register your models here.
admin.site.register(Menu)
admin.site.register(MenuItem)
admin.site.register(Booking)