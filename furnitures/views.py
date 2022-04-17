from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Furniture

# Create your views here.

def all_furniture(request):

    furnitures = Furniture.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn´t enter any search criteria!")
                return redirect(reverse('furnitures'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            furnitures = furnitures.filter(queries)

    context = {
        'furnitures': furnitures,
        'search_term': query,
    }

    return render(request, 'furnitures/furnitures.html', context)


def furniture_detail(request, furniture_id):

    furniture = get_object_or_404(Furniture, pk=furniture_id)

    context = {
        'furniture': furniture,
    }

    return render(request, 'furnitures/furniture_detail.html', context)
