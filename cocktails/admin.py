from django.contrib import admin
from .models import Cocktail
from .models import Comment

# Register your models here.
admin.site.register(Cocktail)
admin.site.register(Comment)