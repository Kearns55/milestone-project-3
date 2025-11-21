from django import forms
from .models import Comment, Cocktail


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class CocktailForm(forms.ModelForm):
    class Meta:
        model = Cocktail
        fields = (
            'name', 'description', 'image', 'ingredients',
            'garnish', 'instructions', 'glass_type',
            'source_type', 'category'
        )
