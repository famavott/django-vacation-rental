"""Views for vacation rental app."""
from django.shortcuts import render


def home(request):
    """Return home page."""
    return render(request, 'vacation_rental/index.html')


def gallery(request):
    """Return gallery page."""
    return render(request, 'vacation_rental/gallery.html')
