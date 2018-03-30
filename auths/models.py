from django.db import models


class BasicUser(models.Model):

    def __init__(self):
        self.user_name = models.CharField(max_length=200)
        self.user_email = models.CharField(max_length=200)
        self.user_pass = models.CharField(max_length=200)

    def __str__(self):
        return self.user_email

    def get_user_name(self):
        return user_name

    def get_user_email(self):
        return user_email

    def get_user_pass(self):
        return user_pass

    def set_user_name(self, name):
        self.user_name = name

    def set_user_email(self, email):
        self.user_email = email

    def set_user_pass(self, password):
        self.user_pass = password
