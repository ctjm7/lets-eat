from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=120, verbose_name='Name')
    cooking_time = models.PositiveIntegerField(help_text='in minutes', verbose_name='Cooking Time')
    ingredients = models.CharField(max_length=350, verbose_name='Ingredients')
    description = models.TextField(default='')
    pic = models.ImageField(upload_to='recipes', default='no_pic.jpeg')

    #@property
    def calculate_difficulty(self):
      ingredients = self.ingredients.split(', ')
      if self.cooking_time < 10 and len(ingredients) < 4:
        difficulty = 'Easy'
      elif self.cooking_time < 10 and len(ingredients) >= 4:
        difficulty = 'Medium'
      elif self.cooking_time >= 10 and len(ingredients) < 4:
        difficulty = 'Intermediate'
      elif self.cooking_time >= 10 and len(ingredients) >=4:
        difficulty = 'Hard'
      return difficulty

    def __str__(self):
      return str(self.name)

    def get_absolute_url(self):
       return reverse('recipes:detail', kwargs={'pk': self.pk})
