from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from users.models import User 



# Create your views here.

def login_view(request):

    if request.user.is_authenticated:
        return redirect('/profile')
    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/profile')
        else:
            return render(request, 'login.html', {'form': login_form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
     return render(request, 'login.html')

def userprofile(request):
    user = User.objects.get(id=3)
    context = {user:'user'}
    return render(request, "profile.html", context)
