from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Question

def index(request):
	#return HttpResponse("Hello world. You are at the polls index.")

	# latest_question_list = Question.objects.order_by('-pub_date')[:5]
	# output = ', '.join([q.question_text for q in latest_question_list])
	# return HttpResponse(output)

	# latest_question_list = Question.objects.order_by('-pub_date')[:5]
	# template = loader.get_template('polls/index.html')
	# context = {'latest_question_list': latest_question_list}
	# return HttpResponse(template.render(context,request))

	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list': latest_question_list}	
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	#return HttpResponse("You are looking at question %s." % question_id)

	# try:
	# 	question = Question.objects.get(pk=question_id)
	# except Question.DoesNotExist:
	# 	raise Http404("Question does not exist")

	question = get_object_or_404(Question, pk=question_id)
	context = {'question': question}
	return render(request, 'polls/detail.html', context)


def results(request, question_id):
	#return HttpResponse("You are looking at the results of question %s." % question_id)
	question = get_object_or_404(Question, pk=question_id)
	context = {'question':question}
	return render(request, 'polls/results.html', context)


def vote(request, question_id):
	#return HttpResponse("You are voting on question %s." % question_id)

	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the voting form
		context = {'question': question,
					'error_message ' : "You didn't select a choice",}
		return render(request, 'polls/detail.html', context)

	else:
		selected_choice.votes += 1
		selected_choice.save()

		return HttpResponseRedirect(reverse('polls:results', args = (question.id,)))