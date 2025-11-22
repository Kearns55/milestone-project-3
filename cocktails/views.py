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
def cocktail_detail(request, pk, slug):
    """ A view to show individual cocktail details """
    cocktail = get_object_or_404(Cocktail, pk=pk)
    # Redirect if cocktail is not approved, except by the author/owner
    if cocktail.author != request.user and not cocktail.approved:
        messages.warning(
            request,
            'This cocktail is not approved yet.')
        return redirect("cocktails")
    # Continue if cocktail is approved
    comments = cocktail.comments.all().order_by("-created_on")
    comment_count = cocktail.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.cocktail = cocktail
            comment.save()
            messages.success(
                request,
                'Comment submitted and awaiting approval')
            return redirect("cocktail_detail", pk=pk, slug=slug)
        messages.error(
            request,
            'There was an error with your comment. Please try again.')
        return redirect("cocktail_detail", pk=pk, slug=slug)
    comment_form = CommentForm()
    template = 'cocktails/cocktail_detail.html'
    context = {
        'cocktail': cocktail,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
    }
    return render(request, template, context)


def add_cocktail(request):
    """ Add cocktail for authenticated users only. """
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged-in to add a cocktail")
        return redirect("cocktails")
    # User is logged in - proceed
    cocktail_form = CocktailForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if cocktail_form.is_valid():
            cocktail_form.instance.author = request.user
            cocktail_form.instance.slug = slugify(request.POST.get("name"))
            new_cocktail = cocktail_form.save()
            cocktail_id = new_cocktail.pk
            cocktail_slug = new_cocktail.slug
            messages.success(request, "Cocktail added successfully!")
            return redirect(cocktail_detail, cocktail_id, cocktail_slug)
        messages.error(request, 'Error adding cocktail, please try again.')
    template = "cocktails/add_cocktail.html"
    context = {
        'form': cocktail_form,
    }
    return render(request, template, context)


def update_cocktail(request, pk, slug):
    """ Update a specific cocktail for authenticated users only. """
    cocktail = get_object_or_404(Cocktail, pk=pk)
    # Check if valid user to edit this cocktail
    if cocktail.author != request.user:
        messages.error(request, "Access Denied: Not your cocktail")
        return redirect("cocktails")
    # Correct user, proceed with update
    cocktail_form = CocktailForm(request.POST or None,
                                 request.FILES or None,
                                 instance=cocktail)
    if request.method == 'POST':
        if cocktail_form.is_valid():
            cocktail_form.instance.approved = False
            cocktail_form.instance.slug = slugify(request.POST.get("name"))
            cocktail_form.save()
            messages.success(
                request,
                "Cocktail updated successfully, and pending!"
            )
            return redirect(cocktail_detail, pk, slug)
        messages.error(request, 'Error updating cocktail, please try again.')
    template = "cocktails/update_cocktail.html"
    context = {
        'form': cocktail_form,
        'cocktail': cocktail,
    }
    return render(request, template, context)


def delete_cocktail(request, pk, slug):
    """ Delete a specific cocktail for authenticated users only. """
    cocktail = get_object_or_404(Cocktail, pk=pk)
    # Check if valid user to delete this cocktail
    if cocktail.author != request.user:
        messages.error(request, "Access Denied: Not your cocktail")
        return redirect("cocktails")
    # Correct user, proceed with delete
    cocktail.delete()
    messages.success(
        request,
        "Cocktail deleted successfully!"
    )
    return redirect('cocktails')


class CategoryView(generic.ListView):
    model = Cocktail
    template_name = "cocktails/category.html"
    context_object_name = "cocktails"

    def get_queryset(self):
        return Cocktail.objects.filter(
            category_id=self.kwargs["pk"],
            approved=True)
        
    def get_context_data(self, **kwargs):
        from .models import Category
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.get(pk=self.kwargs["pk"])
        return context
