from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from furnitures.models import Furniture

def dolly_contents(request):

    dolly_items = []
    total = 0
    furniture_count = 0
    dolly = request.session.get('dolly', {})

    for item_id, quantity in dolly.items():
        furniture = get_object_or_404(Furniture, pk=item_id)
        total += quantity * furniture.price
        furniture_count += quantity
        dolly_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'furniture': furniture,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_difference = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_difference = 0

    grand_total = delivery + total

    context = {
        'dolly_items': dolly_items,
        'total': total,
        'furniture_count': furniture_count,
        'delivery': delivery,
        'free_delivery_difference': free_delivery_difference,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context