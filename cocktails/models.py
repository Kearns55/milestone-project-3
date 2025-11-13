from django.db import models
from django.contrib.auth.models import User
# from cloudinary.models import CloudinaryField


class GlassType(models.Model):
    """
    Glass Type model. Some examples:
    highball, lowball, rocks, old fashioned, martini, cocktail, coupe, collins,
    margarita, hurricane, wine glass, flute, nick & nora, shot glass, tumbler,
    copper mug, snifter, tiki mug
    """
    name = models.CharField(
        max_length=100, unique=True, null=False, blank=False
    )

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    Category model. Some examples:
    classic, modern, mocktail, fruity, sour, bitter, herbal, spicy, sweet,
    bubbly, sparkling, creamy, dessert, tropical, tiki, low-abv, frozen,
    aperitif, digestif, brunch, party
    """
    name = models.CharField(
        max_length=100, unique=True,
        null=False, blank=False
    )

    def __str__(self):
        return self.name


class SourceType(models.Model):
    """
    Source Type model. Some examples:
    own recipe, book, website/blog, video/YouTube, bar menu, friend/family,
    bartender, brand/label, magazine, competition, social media, other
    """
    name = models.CharField(
        max_length=100, unique=True,
        null=False, blank=False
    )

    def __str__(self):
        return self.name


class Cocktail(models.Model):
    """
    Cocktail model. The main body of each cocktail recipe.
    """
    name = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(null=False, blank=False)

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="cocktails",
    )

    # Free-text: one step per line
    ingredients = models.TextField(
        help_text="One ingredient per line (e.g. '60 ml gin').",
        null=False, blank=False
    )

    garnish = models.TextField(
        blank=True, null=True,
        help_text="Optional. Free text (e.g. 'Lime wedge')."
    )

    # Free-text: one step per line
    instructions = models.TextField(
        help_text="One step per line."
    )

    glass_type = models.ForeignKey(
        GlassType,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="cocktails"
    )

    # image = CloudinaryField(
    #     "image",
    #     default="placeholder",
    #     blank=True, null=True
    # )

    source_type = models.ForeignKey(
        SourceType,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="cocktails"
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="cocktails"
    )

    is_publish = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    # Helpers for templates
    def ingredients_list(self):
        return [
            line.strip()
            for line in self.ingredients.splitlines()
            if line.strip()
        ]

    def instructions_list(self):
        return [
            line.strip()
            for line in self.instructions.splitlines()
            if line.strip()
        ]