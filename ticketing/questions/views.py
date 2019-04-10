from django.shortcuts import render
from .models import Question


def completed(request):
    questions = Question.objects.filter(status=True)
    context = {"questions": questions}
    return render(request, "completed.html", context)
