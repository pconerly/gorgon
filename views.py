#from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime

def hello(request):
    return HttpResponse("Hello world")

def maps(request):
    return render_to_response('maps.html')

def current_datetime(reqyest):
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

def default(request):
    #t = loader.get_template('default.html')
    return render_to_response('default.html')
