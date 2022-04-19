from decimal import Decimal
from django.conf import settings

def dolly_contents(request):

    dolly_items = []
    total = 0
    furniture_count = 0

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