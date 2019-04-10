from django.shortcuts import render
from .models import Question
from django.contrib.auth.decorators import login_required


def completed(request):
    questions = Question.objects.filter(status=True)
    context = {"questions": questions}
    return render(request, "completed.html", context)
