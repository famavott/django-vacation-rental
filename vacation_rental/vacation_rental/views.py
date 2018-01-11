"""Views for vacation rental app."""
from django.shortcuts import render


def home(request):
    """Return home page."""
    return render(request, 'vacation_rental/base.html')
