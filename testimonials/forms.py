from django import forms
from .models import UserTestimonial


class TestimonialForm(forms.ModelForm):
    """
    Form for users to leave a testimonial
    """
    rating = forms.ChoiceField(choices=((1, "1 Star"), (2, "2 Stars"), (3, "3 Stars"), (4, "4 Stars"), (5, "5 Stars")), initial=3)
    
    class Meta:
        model = UserTestimonial
        fields = ['content', 'rating']
    