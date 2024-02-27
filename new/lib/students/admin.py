from django.contrib import admin

# Register your models here.
from students.models import CustomUser
admin.site.register(CustomUser)