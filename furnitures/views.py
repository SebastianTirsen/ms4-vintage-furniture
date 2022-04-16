from django.shortcuts import render
from .models import Furniture

# Create your views here.

def all_furniture(request):

    furnitures = Furniture.objects.all()

    context = {
        'furnitures': furnitures,
    }

    return render(request, 'furnitures/furnitures.html', context)
