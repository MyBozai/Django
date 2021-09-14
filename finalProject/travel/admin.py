from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.User)
admin.site.register(models.PlaceAddress)
admin.site.register(models.Search)