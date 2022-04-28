from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .models import Furniture, Category, Support
from .forms import FurnitureForm


# Create your views here.

def all_furniture(request):

    furnitures = Furniture.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                furnitures = furnitures.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            furnitures = furnitures.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            furnitures = furnitures.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('furnitures'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            furnitures = furnitures.filter(queries)
    
    current_sorting = f'{sort}_{direction}'

    context = {
        'furnitures': furnitures,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'furnitures/furnitures.html', context)


def furniture_detail(request, furniture_id):

    furniture = get_object_or_404(Furniture, pk=furniture_id)

    context = {
        'furniture': furniture,
    }

    return render(request, 'furnitures/furniture_detail.html', context)


class SupportCreateView(CreateView):
    model = Support
    fields = ('name', 'description')
    template_name = 'support.html'
    success_url = reverse_lazy('home')


def add_furniture(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = FurnitureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added furniture!')
            return redirect(reverse('add_furniture'))
        else:
            messages.error(request, 'Failed to add furniture. Please ensure the form is valid.')
    else:
        form = FurnitureForm()
        
    template = 'furnitures/add_furniture.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_furniture(request, furniture_id):
    """ Edit a product in the store """
    furniture = get_object_or_404(Furniture, pk=furniture_id)
    if request.method == 'POST':
        form = FurnitureForm(request.POST, request.FILES, instance=furniture)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated furniture!')
            return redirect(reverse('furniture_detail', args=[furniture.id]))
        else:
            messages.error(request, 'Failed to update furniture. Please ensure the form is valid.')
    else:
        form = FurnitureForm(instance=furniture)
        messages.info(request, f'You are editing {furniture.name}')

    template = 'furnitures/edit_furniture.html'
    context = {
        'form': form,
        'furniture': furniture,
    }

    return render(request, template, context)
