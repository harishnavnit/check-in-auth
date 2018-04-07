from django.views import View
from django.shortcuts import render
from django.http import HttpResponse

from auths.models import BasicUser


class LoginView(View):
    authenticated = False
    template_name = 'auths/index.html'

    def authenticate(self, user_email, user_pass):
        try:
            BasicUser.objects.get(user_email=user_email, user_pass=user_pass)
        except BasicUser.DoesNotExist:
            print("User not found")
            return False
        return True


    def get(self, request):
        try:
            user_email = request.GET['email']
            user_pass  = request.GET['pass']

            self.authenticated = self.authenticate(user_email, user_pass)
        except KeyError as err:
            print("email/password not provided : ", err)

        return render(request, self.template_name,
                     {'authenticated': self.authenticated})
