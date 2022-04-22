from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_dolly, name='view_dolly'),
    path('add/<item_id>', views.put_on_dolly, name='put_on_dolly'),
    path('remove/<item_id>', views.remove_from_dolly, name='remove_from_dolly'),
]
