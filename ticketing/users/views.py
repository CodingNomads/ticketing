from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from users.models import User 



# Create your views here.

def login(request):
    print("hello")
    if request.user.is_authenticated:
        return redirect('/profile')
    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/profile')
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def logout(request):
    logout(request)
    return render('/login')

def userprofile(request):
    user = User.objects.get(id=3)
    context = {user:'user'}
    return render(request, "profile.html", context)

