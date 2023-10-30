from django.shortcuts import render
from products.models import Product


def index(request):
    """ view to return the index page """
    sale_products = Product.objects.filter(on_sale=True)[:4]
    return render(request, 'home/index.html', {'sale_products': sale_products})
