from . import views
from django.urls import path
from .views import CategoryView


urlpatterns = [
    path('', views.CocktailListView.as_view(), name='cocktails'),
    path(
        '<int:pk>/<slug:slug>/',
        views.cocktail_detail,
        name='cocktail_detail'
    ),
    path('add_cocktail/', views.add_cocktail, name='add_cocktail'),
    path(
        'update_cocktail/<int:pk>/<slug:slug>/',
        views.update_cocktail,
        name='update_cocktail'
    ),
    path(
        'delete_cocktail/<int:pk>/<slug:slug>/',
        views.delete_cocktail,
        name='delete_cocktail'
    ),
    path(
        "category/<int:pk>/", 
        CategoryView.as_view(),
        name="category"),
]
