from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from myapp.models import Category, Shop, ShopItem
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required

from mysite.forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages

def register_view(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken. Please choose a different one.")
                return render(request, "register.html", {"form": form})
            
            user = User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, "Form submitted successfully!")
            # user=form.save()
            login(request,user)
            return redirect('dashboard')
        else:
            print(form.errors)
    else:
        initial_data={"username":"","email":"","password1":"","password2":""}
        form=RegistrationForm(initial=initial_data)
    return render(request,"register.html",{"form":form})

def login_view(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('dashboard')
    else:
        form=AuthenticationForm()
    return render(request,"login.html",{"form":form})

# @login_required(login_url='login')
def dashboard(request):
    print(f"login=-=---{request.user.is_authenticated}")
    print(f"session item=----{request.session.items()}")
    # if not request.user.is_authenticated:
    #     return redirect('login')
    return render(request,"dashboard.html")

def logout_view(request):
    logout(request)
    return redirect("login")

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