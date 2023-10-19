from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """ view for the shopping bag """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your Basket!')

    request.session['bag'] = bag
    return redirect(redirect_url)


def update_bag(request, item_id):
    """Adjust the quantity of product in the shopping bag"""

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        if item_id in bag:
            del bag[item_id]

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove a product from the shopping cart"""

    try:
        bag = request.session.get('bag', {})

        if item_id in bag:
            del bag[item_id]

            request.session['bag'] = bag
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=404)

    except Exception as e:
        return HttpResponse(status=500)
