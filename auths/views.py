from django.shortcuts import render
from django.http import HttpResponse

from auths.models import BasicUser


def authenticate(user_email, user_pass):
    try:
        BasicUser.objects.get(user_email=user_email, user_pass=user_pass)
    except BasicUser.DoesNotExist:
        print("User not found")
        return False

    return True

def login(request):
    try:
        authenticated = False
        user_email = request.GET['email']
        user_pass  = request.GET['pass']

        authenticated = authenticate(user_email, user_pass)
    except KeyError as err:
        print("GET parameters not found : ", err)

    return render(request, 'auths/index.html', {'authenticated' : authenticated})
