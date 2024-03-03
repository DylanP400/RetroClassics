from django.db import models
from django.contrib.auth.models import User


class UserTestimonial(models.Model):
    """
    Model for Users to leave testimonials
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField(choices=(
        (1, "1 Star"), (2, "3 Stars"), (3, "3 Stars"),
        (4, "4 Stars"), (5, "5 Stars")), null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Testimonial by {self.user.username}"
