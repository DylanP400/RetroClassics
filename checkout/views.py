from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from .forms import OrderForm
from django.conf import settings


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    bag = request.session.get('bag', {})
    if not bag:
        message.error(request, "Your bag is empty right now")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'stripe_secret_key': stripe_secret_key,
    }

    return render(request, template, context)
