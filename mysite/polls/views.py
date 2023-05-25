from django.shortcuts import get_object_or_404, render
# from django.http import HttpResponse, Http404
from django.http import HttpResponse
from django.template import loader

from .models import Question


# Create your views here.

def index(request):
    # latest_question_list = Question.objects.order_by("-pub_date")[:5]
    question = get_object_or_404(Question)
    template = loader.get_template("polls/index.html")
    context = {
        "question": question,
    }

    # return HttpResponse(template.render(context, request))
    # ou : return HttpResponse(request, "polls/index.html", context)
    return render(request, "polls/index.html", context)


"""
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    return HttpResponse(request, "pools/detail.html", {"question": question})
"""


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(question, "polls/detail.html", {"question": question})


def results(request, question_id):
    return HttpResponse("You're voting at the results of question %s." % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
