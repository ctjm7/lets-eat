from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe
from .forms import RecipeSearchForm, AddRecipeForm
import pandas as pd
import string
from .utils import get_chart
import os
from django.conf import settings


# Create your views here.
def home(request):
    return render(request, 'recipes/recipes_home.html')

class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/main.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(RecipeListView, self).get_context_data(*args, **kwargs)
        context = {}
        names_list = list(Recipe.objects.values_list('name', flat=True))
        context['objects'] = Recipe.objects.all()

        def name_to_jpg(data):
            pic_name = []
            for x in data:
                pic_name.append(str(x).replace(' ', '_') + '.jpg')
            return pic_name

        object_names = name_to_jpg(names_list)
        pic_urls = os.listdir(os.path.join(settings.STATIC_ROOT, "recipes/images/"))
        pic_urls = ['recipes/images/'+ object_name for object_name in object_names]

        context['pic_urls'] = pic_urls

        return context

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'

def search(request):
    recipe_form = RecipeSearchForm(request.POST or None)
    recipe_df = None
    all_df = None
    chart = None
    number_recipes = []
    all_ingredients = []

    all_qs = Recipe.objects.all()
    all_df = pd.DataFrame(all_qs.values())

    #function for making name in table clickable to recipe details
    def create_clickable(data):
        url_template = ('<a href="/list/{}">{}</a>').format(data['id'], data['name'])
        return url_template

    #format data to send to html
    def html_data(data):
        data = data.rename(columns={
            'name': 'Name',
            'cooking_time': 'Cooking Time',
            'ingredients': 'Ingredients'
        })

        data = data.to_html(columns=['Name', 'Cooking Time', 'Ingredients'], col_space=55,index=False, justify='left',render_links=True, escape=False)
        return data

    #check if the button is clicked
    if request.method == 'POST':
        recipe_name = request.POST.get('recipe_name')
        chart_type = request.POST.get('chart_type')

        #capitalize recipe name input to retrieve data
        recipe_name = string.capwords(recipe_name)

        #retrieve data on input recipe name
        qs = Recipe.objects.filter(name=recipe_name)
        if qs:
            recipe_df = pd.DataFrame(qs.values())

            #creates a list out of the ingredients string in each recipe
            all_df['ingredients'] = all_df['ingredients'].str.split(', ')

            #flattens list to one list of all ingredients
            for sublist in all_df['ingredients']:
                for ingredient in sublist:
                    all_ingredients.append(ingredient)

            #makes list of ingredients from input recipe
            ingredients_list = recipe_df.loc[0, 'ingredients'].split(', ')

            #loop through all ingredients to see how many recipes contain that ingredient
            for ingredient in ingredients_list:
                if ingredient in all_ingredients:
                    count = all_ingredients.count(ingredient)
                    number_recipes.append(count)

            chart = get_chart(chart_type, ingredients_list, number_recipes, labels=ingredients_list)

            recipe_df['name'] = recipe_df.apply(create_clickable, axis=1)
            #formats data that is seen in html table
            recipe_df = html_data(recipe_df)

    all_df['name'] = all_df.apply(create_clickable, axis=1)

    #gives table of all recipes if there is no input recipe by user
    all_df = html_data(all_df)

    #pack up data to be sent to template in the context dictionary
    context = {
        'recipe_form': recipe_form,
        'recipe_df': recipe_df,
        'all_df': all_df,
        'chart': chart,
    }
    return render(request, 'recipes/search.html', context)

def add_recipe(request):
  form = AddRecipeForm(request.POST or None)

  if request.method == 'POST':
    if request.POST.get('add_name') and request.POST.get('add_ingredients'):
      recipe=Recipe()
      recipe.name = string.capwords(request.POST.get('add_name'))
      recipe.cooking_time = request.POST.get('add_cooking_time')
      recipe.ingredients = string.capwords(request.POST.get('add_ingredients'))
      recipe.description = request.POST.get('add_description')
      recipe.save()
      messages.success(request, 'Recipe has been saved')
      return HttpResponseRedirect('/addrecipe/')

  context = {
      'form': form
  }

  return render(request, 'recipes/add_recipe.html', context)
