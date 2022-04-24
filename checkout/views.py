from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    dolly = request.session.get('dolly', {})
    if not dolly:
        messages.error(request, "There's nothing on your dolly at the moment")
        return redirect(reverse('furnitures'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)