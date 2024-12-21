from django.shortcuts import render

# Create your views here.
from myapp.models import Category, Image

# Create your views here.

def home_page(request):
    images=Image.objects.all()
    categories=Category.objects.all()
    data={'images':images,'categories':categories}
    return render(request,"home.html",data)


def category_page(request,cid):
    print(f"Beta hamari pid=---{cid}")
    categories=Category.objects.all()
    category=Category.objects.get(pk=cid)
    images=Image.objects.filter(cat=category)
    data={'images':images,'categories':categories}
    print(f"categories data=-=-----{category}")
    return render(request,"home.html",data)