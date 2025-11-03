from django.shortcuts import render

# Create your views here.

def home(request):
    """Home Page View"""

    return render(request, "index.html")


def about(request):
    """About Page View"""

    return render(request, "about.html")

def services(request):
    """Services page view"""

    return render(request, "service.html")

def contact(request):
    """Contact page view"""

    return render(request, "contact.html")