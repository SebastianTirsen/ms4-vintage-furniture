"""ms4_vintage_furniture URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from furnitures.views import SupportCreateView
from ratings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('furnitures/', include('furnitures.urls')),
    path('dolly/', include('dolly.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('support/', SupportCreateView.as_view(), name='support'),
    path('rating', views.rating,  name='rating'),
    path('insert_data', views.insert_data,  name='insert_data'),
    path('update_data<int:id>', views.update_data,  name='update_data'),
    path('delete_data<int:id>', views.delete_data,  name='delete_data'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
