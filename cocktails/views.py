from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Cocktail


class CocktailListView(generic.ListView):
    queryset = Cocktail.objects.all().filter(approved=True)
    template_name = "cocktails/index.html"
    paginate_by = 6


# Create your views here.
def cocktail_detail(request, slug):
    """ A view to show individual cocktail details """
    
    queryset = Cocktail.objects.all().filter(approved=True)
    cocktail = get_object_or_404(queryset, slug=slug)
    return render(
        request,
        'cocktails/cocktail_detail.html',
        {'cocktail': cocktail},
    )