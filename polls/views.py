from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Question
# Create your views here.

def index(request): 
  lastest_question_list = Question.objects.order_by('-pub_date')[:5]
  # template = loader.get_template('polls/index.html')
  context = {
    'lastest_question_list': lastest_question_list
  }
  # output = ','.join([q.question_text for q in lastest_question_list])
  return render(request, 'polls/index.html', context)

def detail(request, question_id):
  try:
    question = get_object_or_404(Question, pk=question_id)
  except Question.DoesNotExist:
    raise Http404("Question does not exist")
  return render(request, 'polls/detail.html', {'question': question})

def result(request, question_id):
  response = " You're looking at the result of question %s."
  return HttpResponse(response % question_id)

def vote(request, question_id):
  return HttpResponse("You're voting on question %s." % question_id)