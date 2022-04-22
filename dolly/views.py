from django.shortcuts import render, redirect, reverse

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


def remove_from_dolly(request, item_id):
    dolly = request.session.get('dolly', {})
    dolly.pop(item_id)

    request.session['dolly'] = dolly
    return redirect(reverse('view_dolly'))
