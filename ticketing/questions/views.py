from django.shortcuts import render
from .forms import QuestionForm
from .models import Question


# Create your views here.

def pending_questions(request):
    context = {}
    form = QuestionForm
    questions_pending = Question.objects.filter(status=False).order_by("date_added")
    questions_completed = Question.objects.filter(status=True).order_by("date_answered")[:10]


    context["form"] = form
    context["questions_pending"] = questions_pending
    context["questions_completed"] = questions_completed

    return render(request, "pending_questions.html", context=context)