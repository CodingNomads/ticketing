from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from questions.models import Question


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/users/profile')
    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/users/profile')
        else:
            return render(request, 'users/login.html', {'form': login_form})
    else:
        form = AuthenticationForm()
        return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'users/login.html')


def userprofile(request):
    current_userid = request.user.id
    questions = Question.objects.filter(author_id=current_userid)
    context = {'questions': questions}
    return render(request, "users/profile.html", context)
