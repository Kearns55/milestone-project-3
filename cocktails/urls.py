from . import views
from django.urls import path


urlpatterns = [
    path('', views.CocktailListView.as_view(), name='home'),
]