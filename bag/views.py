from django.shortcuts import (
    render,
    redirect,
    reverse,
    HttpResponse,
    get_object_or_404
    )
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """ view for the shopping bag """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your basket!')

    request.session['bag'] = bag
    return redirect(redirect_url)


def update_bag(request, item_id):
    """Adjust the quantity of product in the shopping bag"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request,
            f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        if item_id in bag:
            del bag[item_id]
            messages.error(request, f'Something went wrong!')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove a product from the shopping cart"""

    product = get_object_or_404(Product, pk=item_id)

    try:
        bag = request.session.get('bag', {})

        if item_id in bag:
            del bag[item_id]
            request.session['bag'] = bag
            messages.success(request, f'Removed {product.name} from basket')
            return HttpResponse(status=200)

        else:
            messages.error(request, f'Something went wrong!')
            return HttpResponse(status=404)

    except Exception as e:
        messages.error(request, f'Something went wrong! {e}')
        return HttpResponse(status=500)
