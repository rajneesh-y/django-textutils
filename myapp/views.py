from django.shortcuts import render,HttpResponse

# Create your views here.
from myapp.models import Category, Shop, ShopItem

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

def shopitem(request,unique_id):
    shopitems=Shop.objects.get(unique_id=unique_id)
    items=ShopItem.objects.filter(shopId=shopitems.id)
    data={"items":items}
    return render(request,"shopitem.html",data)