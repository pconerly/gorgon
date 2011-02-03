#from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime
import time
from django.core import serializers
from django.utils import simplejson

def hello(request):
    return HttpResponse("Hello world")

def maps(request):
    return render_to_response('maps.html')

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

class HandleQuerySets(simplejson.JSONEncoder):
    """ simplejson.JSONEncoder extension: handle querysets """
    def default(self, obj):
        if isinstance(obj, QuerySet):
            return serializers.serialize("json", obj, ensure_ascii=False)
        
        return simplejson.JSONEncoder.default(self, obj)

def homework(request):
    try:
        a = int(request.GET['a'])
        b = int(request.GET['b'])
    except ValueError:
        raise Http500()
    answer = a+b
    #jsons = serializers.get_serializer("json")()
    ptime = time.time()
    queryset = {"result":answer, "uwnetid":"pconerly", "time":ptime}
    test = simplejson.dumps(queryset, cls=HandleQuerySets)
    #result = jsons.serialize(queryset, ensure_ascii=False) #, stream=response)
    return HttpResponse(test, mimetype="text/html")
    #html = "<html><body>Answer is %s </body></html>" % answer
    #return HttpResponse(html)

def default(request):
    #t = loader.get_template('default.html')
    return render_to_response('default.html')
