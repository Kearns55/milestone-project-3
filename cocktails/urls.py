from . import views
from django.urls import path


urlpatterns = [
    path('', views.CocktailListView.as_view(), name='home'),
    path('cocktail/<slug:slug>/', views.cocktail_detail, name='cocktail_detail'),
]