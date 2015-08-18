from django.shortcuts import get_object_or_404, render

from polls.models import Question

# Why do we use a helper function get_object_or_404() instead of automatically
# catching the ObjectDoesNotExist exceptions at a higher level, or having the
# model API raise Http404 instead of ObjectDoesNotExist?

# Because that would couple the model layer to the view layer.
# One of the foremost design goals of Django is to maintain loose coupling.
# Some controlled coupling is introduced in the django.shortcuts module.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
    })
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
