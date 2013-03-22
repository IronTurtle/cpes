from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from cpe400.models import Problem, Answer
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404

# Create your views here.
def index(request):
	latest_problem_list = Problem.objects.all().order_by('-pub_date')[:5]
	return render_to_response('cpe400/index.html', 
			{'latest_problem_list': latest_problem_list})

def detail(request, problem_id):
	p = get_object_or_404(Problem, pk=problem_id)
	return render_to_response('cpe400/detail.html',
			{'problem': p},
			context_instance=RequestContext(request))

def results(request, problem_id):
	return HttpResponse("Thank you for participating in CPEs Challege: %s" % problem_id)

def answer(request, problem_id):
	p = get_object_or_404(Problem, pk= problem_id)
	try:
		username = request.POST['username']
		answer = request.POST['answer']
		a = Answer(problem=p, answer=answer, user=username)
	except (KeyError, Answer.DoesNotExist):
		return render_to_response('cpe400/detail.html', {
			'problem': p,
			'error_message': "Username not found",
			}, context_instance=RequestContext(request))
	else:
		a.save()
		return HttpResponseRedirect(reverse('cpe400.views.results', args=(p.id,)))