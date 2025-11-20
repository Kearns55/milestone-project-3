from . import views
from django.urls import path


urlpatterns = [
    path('', views.CocktailListView.as_view(), name='cocktails'),
    path(
        '<int:pk>/<slug:slug>/',
        views.cocktail_detail,
        name='cocktail_detail'
    ),
    path('add_cocktail/', views.add_cocktail, name='add_cocktail'),
]