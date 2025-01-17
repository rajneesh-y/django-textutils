"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from myapp.views import category_page, dashboard, home_page, login_view, logout_view, shopitem,register_view
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home_page),
    path('textutils', views.index, name='index'),
    path('analyze', views.analyze, name='analyze'),
    # path('upload', views.upload_image,name="upload"),
    path("category/<int:cid>", category_page),
    path("shopitem/<str:unique_id>/", shopitem),
    path('register', register_view, name='register'),
    # path('dashboard', views.HomeView.as_view(), name='dashboard'),
    path('dashboard', dashboard, name='dashboard'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),

]


from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.index_title="My Shop"
admin.site.site_header="My Shop Admin"
admin.site.site_title="Shop Admin"