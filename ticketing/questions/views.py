from django.shortcuts import render
from .forms import QuestionForm
from .models import Question
from django.contrib.auth.decorators import login_required

# Create your views here.

def pending_questions(request):
    context = {}

    if request.method == "POST":
        form = QuestionForm(data=request.POST)
        if form.is_valid():
            post_question = form.save(commit=False)
            new_question = Question(title=post_question.title, description=post_question.description,
                                    author=request.user)
            new_question.save()

    form = QuestionForm
    questions_pending = Question.objects.filter(status=False).order_by("date_asked")
    questions_completed = Question.objects.filter(status=True).order_by("date_answered")[:5]


    context["form"] = form
    context["questions_pending"] = questions_pending
    context["questions_completed"] = questions_completed

    return render(request, "pending_questions.html", context=context)

def completed(request):
    questions = Question.objects.filter(status=True)
    context = {"questions": questions}
    return render(request, "completed.html", context)

