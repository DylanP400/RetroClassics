from django.urls import path
from .views import (
    UserTestimonialsListView,
    UserTestimonialsDetailView,
    add_testimonial,
    edit_testimonial,
    delete_testimonial,
)
from . import views

urlpatterns = [
path('add_testimonial/', views.add_testimonial, name='add_testimonial'),
path(
    'UserTestimonials/<int:pk>/',
    UserTestimonialsDetailView.as_view(),
    name='testimonials_detail'
    ),
path(
    'edit_testimonial/<int:pk>',
    views.edit_testimonial.as_view(),
    name='edit_testimonial'
    ),
     path(
        'delete_testimonial/<int:pk>',
        views.delete_testimonial.as_view(),
        name='delete_testimonial'
        ),
path('', UserTestimonialsListView.as_view(), name='home-page'),
]