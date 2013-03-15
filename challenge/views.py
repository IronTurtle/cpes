from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render

from challenge.models import Problem, Answer, User

def index(request):
	latest_problem_list = Problem.objects.all()
	context = {'latest_problem_list': latest_problem_list}
	return render(request, 'challenge/index.html', context)

def problem(request, problem_id):
	p = Problem.objects.get(pk=problem_id);
	return HttpResponse("You are at %s problem." % p.pub_date)