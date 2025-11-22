from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class GlassType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class SourceType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Cocktail(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    image = CloudinaryField('image', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True)

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="cocktails",
    )

    ingredients = models.TextField(
        help_text="One ingredient per line."
    )

    garnish = models.TextField(
        blank=True, null=True,
        help_text="Optional. Free text."
    )

    instructions = models.TextField(
        help_text="One step per line."
    )

    glass_type = models.ForeignKey(
        GlassType,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="cocktails"
    )

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

    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        if not self.name:
            return "No Name Cocktail"
        vowels = 'AEIOU'
        article = 'an' if self.name[0] in vowels else 'a'
        return f"This recipe for {article} {self.name} | was written by {self.author}"

    # Helpers — MUST be inside the class
    def ingredients_list(self):
        return [
            line.strip()
            for line in self.ingredients.splitlines()
            if line.strip()
        ]


class Comment(models.Model):
    """ Comments model for user comments on cocktails. """
    cocktail = models.ForeignKey(
        Cocktail,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="commenter",
    )
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created_on']   

    def __str__(self):
        return f"Comment by {self.author.username} on {self.cocktail.name}"
