from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.decorators import login_required
from .models import UserTestimonial
from .forms import TestimonialForm
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse, reverse_lazy

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
        'form': form,
    }
    return render(request, 'add_testimonial.html', context)


class edit_testimonial(UserPassesTestMixin, UpdateView):
    """
    View for updating a Testimonial.
    """
    model = UserTestimonial
    fields = ['content', 'rating']

    def test_func(self):
        testimonial = self.get_object()
        return self.request.user == testimonial.user

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request,
            'You have successfully updated your testimonial'
            )
        return response

    def get_success_url(self):
        return reverse('edit_testimonial', args=[self.object.pk])


class delete_testimonial(UserPassesTestMixin, DeleteView):
    """
    View for deleting a Testimonial.
    """
    model = UserTestimonial
    success_url = reverse_lazy('profile')

    def test_func(self):
        testimonial = self.get_object()
        return self.request.user == testimonial.user

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'You have successfully deleted your testimonial')
        return super().delete(request, *args, **kwargs)