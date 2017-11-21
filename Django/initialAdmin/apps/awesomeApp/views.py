from django.shortcuts import HttpResponse

# Create your views here.


def index(request):
    print request.META['HTTP_HOST']
    print request.META['SERVER_NAME']
    print request.META['REQUEST_METHOD']
    print request.META['CONTENT_TYPE']
    print request.META['REMOTE_ADDR']
    print request.META['SERVER_PORT']
    return HttpResponse("Well, here you are, then.")
