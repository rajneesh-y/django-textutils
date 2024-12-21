from django.contrib import admin

# Register your models here.
from myapp.models import Category, Image

admin.site.register([Category,Image])
