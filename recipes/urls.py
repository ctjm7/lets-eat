from django.urls import path
from .views import home, search, add_recipe
from .views import RecipeListView, RecipeDetailView

app_name = 'recipes'

urlpatterns = [
    path('', home, name='home'),
    path('list/', RecipeListView.as_view(), name='list'),
    path('list/<pk>', RecipeDetailView.as_view(), name='detail'),
    path('search/', search, name='search'),
    path('addrecipe/', add_recipe, name='add_recipe'),
]
