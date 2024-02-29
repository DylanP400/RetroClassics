from django.shortcuts import render
from products.models import Product
from testimonials.models import UserTestimonial


def index(request):
    """ view to return the index page """
    sale_products = Product.objects.filter(on_sale=True)[:4]
    testimonials = UserTestimonial.objects.all().order_by('-date_created')[:3]

    context = {
        'sale_products': sale_products,
        'testimonials': testimonials,
        }
    return render(request, 'home/index.html', context)
