from django.contrib import admin
from django.contrib.auth.models import Group
from my_app.models import Dostavka
# Register your models here.


admin.site.unregister([Group])
admin.site.register([Dostavka])

