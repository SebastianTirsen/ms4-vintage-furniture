from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_dolly, name='view_dolly'),
    path('add/<item_id>', views.put_on_dolly, name='put_on_dolly'),
]
