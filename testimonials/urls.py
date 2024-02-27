from django.urls import path
from .views import (
    UserTestimonialsListView,
    UserTestimonialsDetailView,
    add_testimonial,
)
from . import views

urlpatterns = [
path('add_testimonial/', views.add_testimonial, name='add_testimonial'),
path(
    'UserTestimonials/<int:pk>/',
    UserTestimonialsDetailView.as_view(),
    name='testimonials-detail'
    ),
path('', UserTestimonialsListView.as_view(), name='home-page'),
]