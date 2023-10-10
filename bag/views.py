from django.shortcuts import render


def view_bag(request):
    """ view for the shopping bag """
    
    return render(request, 'bag/bag.html')