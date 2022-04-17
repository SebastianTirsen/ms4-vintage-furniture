from django.shortcuts import render, get_object_or_404
from .models import Furniture

# Create your views here.

def all_furniture(request):

    furnitures = Furniture.objects.all()

    context = {
        'furnitures': furnitures,
    }

    return render(request, 'furnitures/furnitures.html', context)


def furniture_detail(request, furniture_id):

    furniture = get_object_or_404(Furniture, pk=furniture_id)

    context = {
        'furniture': furniture,
    }

    return render(request, 'furnitures/furniture_detail.html', context)
