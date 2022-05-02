from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from furnitures.models import Furniture

# Create your views here.


def view_dolly(request):

    return render(request, 'dolly/dolly.html')


def put_on_dolly(request, item_id):
    furniture = get_object_or_404(Furniture, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    dolly = request.session.get('dolly', {})

    if item_id in list(dolly.keys()):
        dolly[item_id] += quantity
    else:
        dolly[item_id] = quantity
        messages.success(request,
                         f'You put { furniture.name } on your Dolly! ')

    request.session['dolly'] = dolly
    return redirect(redirect_url)


def remove_from_dolly(request, item_id):
    try:
        furniture = get_object_or_404(Furniture, pk=item_id)
        dolly = request.session.get('dolly', {})
        dolly.pop(item_id)
        messages.success(request,
                         f'Unloaded { furniture.name } from your Dolly!')

        request.session['dolly'] = dolly
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error unloading item: {e} from your Dolly!')
    return HttpResponse(status=500)
