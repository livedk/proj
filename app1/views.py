from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from tasks import *


# Create your views here.

def index(request, template_name="app1/index.html"):
    msg = 'hello world'
    return render_to_response(template_name, {
        "msg": msg,
    }, context_instance=RequestContext(request))


def json(request):
    result = {'t': 't'}
    return JsonResponse(result)


def rediret(request):
    next = "index"
    return HttpResponseRedirect(next)

def async_add(request):
    x = request.GET.get('x', 1)
    y = request.GET.get('y', 1)
    x = int(x)
    y = int(y)
    r = add.delay(x, y)
    result = {'task_id': r.id}
    while 1:
        if r.ready():
            result['value'] = r.get()
            return JsonResponse(result)