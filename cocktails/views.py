from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Cocktail
from .forms import CommentForm


class CocktailListView(generic.ListView):
    queryset = Cocktail.objects.all().filter(approved=True)
    template_name = "cocktails/index.html"
    paginate_by = 6


# Create your views here.
def cocktail_detail(request, slug):
    """ A view to show individual cocktail details """
    queryset = Cocktail.objects.all().filter(approved=True)
    cocktail = get_object_or_404(queryset, slug=slug)
    comments = cocktail.comments.all().order_by("-created_on")
    comment_count = cocktail.comments.filter(approved=True).count()
    if request.method == "cocktail":
        comment_form = CommentForm(data=request.cocktail)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.cocktail = cocktail
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
    
    comment_form = CommentForm()
    return render(
        request,
        'cocktails/cocktail_detail.html',
        {
            'cocktail': cocktail,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            },
    )