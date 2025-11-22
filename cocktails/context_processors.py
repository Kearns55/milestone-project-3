from .models import Category


"""Context processor to add categories to the navbar."""


def categories(request):
    return {
        "categories": Category.objects.all()
    }
