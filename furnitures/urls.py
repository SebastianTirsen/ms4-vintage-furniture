from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_furniture, name='furnitures'),
    path('<int:furniture_id>/', views.furniture_detail, name='furniture_detail'),
    path('add/', views.add_furniture, name='add_furniture'),
]