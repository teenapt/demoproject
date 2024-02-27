from django.contrib import admin
from shop.models import Category,product
from django.http import HttpResponse
admin.site.register(Category)
admin.site.register(product)