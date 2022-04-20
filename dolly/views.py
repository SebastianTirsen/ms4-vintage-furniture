from django.shortcuts import render, redirect

# Create your views here.

from django.shortcuts import render

# Create your views here.

def view_dolly(request):

    return render(request, 'dolly/dolly.html')

def put_on_dolly(request, item_id):
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    dolly = request.session.get('dolly', {})

    if item_id in list(dolly.keys()):
        dolly[item_id] += quantity
    else:
        dolly[item_id] = quantity

    request.session['dolly'] = dolly
    return redirect(redirect_url)
