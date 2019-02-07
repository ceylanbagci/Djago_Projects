from django.contrib import admin

# Register your models here.
from .models import Customer,Book


admin.site.register(Customer)
admin.site.register(Book)
