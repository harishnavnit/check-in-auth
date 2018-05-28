from django.views import View
from django.shortcuts import render
from django.http import HttpResponse


class LocationView(View):
    current_location = {}
    template_name = 'hubs/location.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        self.current_location['latitude'] = request.POST['coords[latitude]']
        self.current_location['longitude'] = request.POST['coords[longitude]']
        self.current_location['timestamp'] = request.POST['timestamp']

        return HttpResponse(status=200)
