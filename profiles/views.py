from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from testimonials.models import UserTestimonial
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required

from checkout.models import Order


@login_required
def profile(request):
    """ Display the users profile """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please make sure the form\
                is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    user_testimonials = UserTestimonial.objects.filter(user=request.user).order_by('-date_created')

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'user_testimonials': user_testimonials,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'

    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
