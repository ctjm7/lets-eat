from django import forms

#specified as a tuple for chart choices
CHART__CHOICES = (
   ('#1', 'Bar chart'),    # when user selects "Bar chart", it is stored as "#1"
   ('#2', 'Pie chart'),
   ('#3', 'Line chart'),
   )

class RecipeSearchForm(forms.Form):
    recipe_name = forms.CharField(max_length=120)
    chart_type = forms.ChoiceField(choices=CHART__CHOICES)

class AddRecipeForm(forms.Form):
    add_name = forms.CharField(max_length=120, required=True, widget=forms.TextInput(attrs={'size': '40'}))
    add_ingredients = forms.CharField(max_length=350, required=True, widget=forms.TextInput(attrs={'size': '100'}))
    add_cooking_time = forms.IntegerField()
    add_description = forms.CharField(widget=forms.Textarea(attrs={"cols":"55", "rows": "15"}))
