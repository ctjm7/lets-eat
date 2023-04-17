# Recipe App

This is an application built with Python that utilizes the Django Framework.

It allows users to create an account. They can add and modify recipes in their account. The user will input recipe name, ingredients and cooking time. The app will calculate the difficulty of the recipe based on the input. The user will be able to search for a recipe. A chart will be displayed with the number of recipes containing the ingredients in the searched recipe.

## Setting up your environment

1. Install Python version 3.8.7
2. Create a virtual environment on your computer in the designated project folder
    `mkvirtualenv {environment-name}`
3. Install Django with `pip install django`
4. Clone repository: git clone https://github.com/ctjm7/recipe-app.git
5. Install all Project dependencies inside the project folder: `pip install`
      a) pillow
      b) pandas
      c) matplotlib
6. Convert class models into database tables with `python manage.py migrate`
7. Create a superuser
      a) In project root directory execute command `python manage.py createsuperuser`
      b) `python manage.py runserver` go to “http://127.0.0.1:8000/admin/” to login
8. Add data from the Django site admin with a few recipes after running server `python manage.py runserver` and go to “http://127.0.0.1:8000/admin/”

## Dependencies
```
asgiref             3.6.0
backports.zoneinfo  0.2.1
Brotli              1.0.9
contourpy           1.0.7
cycler              0.11.0
dj-database-url     1.3.0
Django              4.1.7
fonttools           4.39.2
gunicorn            20.1.0
importlib-resources 5.12.0
kiwisolver          1.4.4
matplotlib          3.7.1
numpy               1.24.2
packaging           23.0
pandas              1.5.3
Pillow              9.4.0
pip                 23.0.1
psycopg2-binary     2.9.6
pyparsing           3.0.9
python-dateutil     2.8.2
pytz                2023.2
setuptools          67.1.0
six                 1.16.0
sqlparse            0.4.3
typing_extensions   4.5.0
wheel               0.38.4
whitenoise          6.4.0
zipp                3.15.0
