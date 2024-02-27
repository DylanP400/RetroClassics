from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from .models import UserTestimonial
from .forms import TestimonialForm
from django.contrib import messages

# Create your views here.

class UserTestimonialsListView(ListView):
    """
    List view to display a list of UserTestimonials.
    """
    model = UserTestimonial
    template_name = 'home/templates/index.html'
    context_object_name = 'user_testimonial'
    paginate_by = 3


class UserTestimonialsDetailView(DetailView):
    """
    Detail view to display a single UserTestimonial.
    """
    model = UserTestimonial


@login_required
def add_testimonial(request):
    """
    View for adding a Testimonial.
    """
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.user = request.user
            testimonial.save()
            messages.success(request, 'Thank you for leaving a review')
            return redirect('/')
    else:
        form = TestimonialForm()
    context = {
        'form': form
    }
    return render(request, 'add_testimonial.html', context)
