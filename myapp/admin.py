from django.contrib import admin

# Register your models here.
from myapp.models import Category, Shop,ShopItem

admin.site.register([Category,Shop,ShopItem])
