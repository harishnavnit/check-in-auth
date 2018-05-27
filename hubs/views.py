from django.shortcuts import render
from django.http import HttpResponse


current_location = {}


def index(request):
    return render(request, 'hubs/location.html')


def locations(request):
    if request.method == "POST":
        current_location['latitude'] = request.POST['coords[latitude]']
        current_location['longitude'] = request.POST['coords[longitude]']
        current_location['timestamp'] = request.POST['timestamp']

    return HttpResponse(status=200)
