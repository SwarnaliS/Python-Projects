from django.contrib import admin

from .models import djangoClasses

#Registered the database with the admin
admin.site.register(djangoClasses)
