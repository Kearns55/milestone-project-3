from django.shortcuts import render
from django.views import generic
from .models import Cocktail


class CocktailListView(generic.ListView):
    queryset = Cocktail.objects.all().filter(approved=True)
    template_name = "cocktails/cocktails_list.html"
    context_object_name = "cocktails"


# Create your views here.
