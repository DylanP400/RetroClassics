from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm


# Create your views here.
def profile(request):
    """ Display the users profile """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    order = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'order': order,
        'on_profile_page': True
    }

    return render(request, template, context)
