from django.shortcuts import render, redirect
#Django authentication libraries
from django.contrib.auth import authenticate, login, logout
#Django Form for authentication
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
  #initialize error_message None
  error_message = None
  #form object with username and password fields
  form = AuthenticationForm()

  #when user hits "login" button, then POST request is generated
  if request.method == 'POST':
    form = AuthenticationForm(data=request.POST)
    #check if form is valid
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')

      #Django authenticate function to validate user
      user = authenticate(username=username, password=password)

      #user is authenticated use Django to login
      if user is not None:
        login(request, user)
        return redirect('recipes:list')

    else:
      error_message = 'something went wrong'

  #prepare data to send from view to template
  context = {
    'form': form,
    'error_message': error_message
  }
  return render(request, 'auth/login.html', context)

def logout_view(request):
  #pre-defined Django function to logout
  logout(request)
  return render(request, 'auth/success.html')

def about(request):
  return render(request, 'auth/about.html')
