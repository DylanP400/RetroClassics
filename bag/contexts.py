from decimal import Decimal
from django.conf import settings
from products.models import Game, Product, Console
from django.shortcuts import get_object_or_404


def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    has_console = False
    bag = request.session.get('bag', {})
    cart_console_ids = []

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

        if isinstance(product, Console):
            has_console = True
            cart_console_ids.append(item_id)

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    free_games = 0
    if has_console:
        associated_games = Game.objects.filter(
            associated_console__in=cart_console_ids
            )
        free_games = associated_games.count() * 2

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
        'free_games': free_games,
    }

    return context
