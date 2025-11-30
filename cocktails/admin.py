from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Cocktail, Comment, GlassType, Category, SourceType


@admin.register(Cocktail)
class CocktailAdmin(SummernoteModelAdmin):
    list_display = ('name', 'author', 'created_on', 'glass_type', 'source_type')
    list_filter = ('created_on', 'glass_type', 'source_type', 'author')
    search_fields = ('name', 'description', 'ingredients', 'instructions'
                     , 'author__username')
    summernote_fields = ('instructions', 'description')


# Register your models here.
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(GlassType)
admin.site.register(SourceType)