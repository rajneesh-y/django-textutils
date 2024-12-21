from django.shortcuts import render

# Create your views here.
from myapp.models import Category, Shop

# Create your views here.

def home_page(request):
    Shops=Shop.objects.all()
    categories=Category.objects.all()
    data={'Shops':Shops,'categories':categories}
    return render(request,"home.html",data)


def category_page(request,cid):
    print(f"Beta hamari pid=---{cid}")
    categories=Category.objects.all()
    category=Category.objects.get(pk=cid)
    Shops=Shop.objects.filter(cat=category)
    data={'Shops':Shops,'categories':categories}
    print(f"categories data=-=-----{category}")
    return render(request,"home.html",data)