from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'hubs/location.html')


def locations(request):
    # _status = 200 if request.GET['coordinates'] else 500
    # return HttpResponse(status=_status)
    print("request : ", request)
    return HttpResponse(status=200)
