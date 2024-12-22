from django.db import models
from django.utils.text import slugify
from autoslug import AutoSlugField

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.title

class Shop(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to='images')
    added_date=models.DateTimeField()
    unique_id = models.CharField(max_length=100, unique=True, blank=True, null=True)
    cat=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return f"Shop ID: {self.id} - {self.title} - Unique ID: {self.unique_id}"
    
class ShopItem(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to='images')
    added_date=models.DateTimeField()
    shopId=models.ForeignKey(Shop,on_delete=models.CASCADE)

    def __str__(self):
        return self.title