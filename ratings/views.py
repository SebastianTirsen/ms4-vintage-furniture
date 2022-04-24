from django.shortcuts import render, HttpResponse, redirect
from .models import Rating
from django.contrib import messages


def rating(request):
    all_data = Rating.objects.all()
    ratings = {'all_data':all_data}
    return render(request, "rate.html", ratings)


def insert_data(request):
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        if(name == '' or description == ''):
            messages.warning(request, "Fill in your rating ...")
        else:
            rate = Rating(name=name, description=description)
            rate.save()
    return redirect(rating)


def update_data(request, id):
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        if(name == '' or description == ''):
            messages.warning(request,"Fill in your rating ...")
        else:
            rate = Rating(name = name, description = description, id = id)
            rate.save()

    return redirect(rating)


def delete_data(request, id):
    if request.method == "GET":
        data = Rating.objects.filter(id=id)
        data.delete()
        messages.error(request, 'Your rating was deleted!')
    return redirect(rating)
