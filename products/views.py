from django.shortcuts import render, get_object_or_404
from .models import Product, Game, Console, Category


def all_products(request):
    """view to show all products"""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """view to show all selected product"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/products_detail.html', context)
