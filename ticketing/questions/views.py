from django.shortcuts import render, reverse
from urllib.parse import urlencode
from .forms import QuestionForm
from .models import Question
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


@login_required(login_url="/users/login/")
def pending_questions(request):
    context = {}

    if request.method == "POST":
        form = QuestionForm(data=request.POST)
        if form.is_valid():
            post_question = form.save(commit=False)
            # add helpful link to help students get started solving their own questions... :)
            lmgtfy = "http://lmgtfy.com/?" + urlencode({'q': post_question.title})
            new_question = Question(title=post_question.title, description=post_question.description,
                                    author=request.user, lmgtfy=lmgtfy)
            new_question.save()
            return HttpResponseRedirect(reverse('questions:completed'))

    form = QuestionForm
    questions_pending = Question.objects.filter(status=False).order_by("date_asked")
    questions_completed = Question.objects.filter(status=True).order_by("date_answered")[:5]

    context["form"] = form
    context["questions_pending"] = questions_pending
    context["questions_completed"] = questions_completed

    return render(request, "questions/pending_questions.html", context=context)


@login_required(login_url="/users/login/")
def completed(request):
    questions = Question.objects.filter(status=True)
    context = {"questions": questions}
    return render(request, "questions/completed.html", context)
