from django.shortcuts import render


def home(request):
    """
    Renders the Home page
    """
    template = "home/index.html"
    context = {}
    return render(request, template, context)
