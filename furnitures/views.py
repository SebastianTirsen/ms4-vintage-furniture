from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Furniture, Category

# Create your views here.

def all_furniture(request):

    furnitures = Furniture.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            furnitures = furnitures.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

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
        'current_categories': categories,
    }

    return render(request, 'furnitures/furnitures.html', context)


def furniture_detail(request, furniture_id):

    furniture = get_object_or_404(Furniture, pk=furniture_id)

    context = {
        'furniture': furniture,
    }

    return render(request, 'furnitures/furniture_detail.html', context)
