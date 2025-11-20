from django.shortcuts import redirect, render, get_object_or_404
from django.views import generic
from django.db.models import Q
from django.contrib import messages
from django.utils.text import slugify
from .models import Cocktail
from .forms import CommentForm, CocktailForm


class CocktailListView(generic.ListView):
    template_name = "cocktails/cocktails.html"
    paginate_by = 6

    def get_queryset(self):
        queryset = Cocktail.objects.all()

        if self.request.user.is_authenticated:
            # Show:
            # - all approved cocktails
            # - plus this user's cocktails even if not approved
            return queryset.filter(
                Q(approved=True) | Q(author=self.request.user)
            ).distinct()

        # Guest users only see approved cocktails
        return queryset.filter(approved=True)


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