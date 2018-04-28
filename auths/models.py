from django.db import models


class BasicUser(models.Model):

    user_email = models.CharField(max_length=200,
                                  default="example@example.com")
    user_pass = models.CharField(max_length=200, default="example_pass")

    def __str__(self):
        return self.user_email

    def get_user_email(self):
        return self.user_email

    def get_user_pass(self):
        return self.user_pass

    def set_user_email(self, email):
        self.user_email = email

    def set_user_pass(self, password):
        self.user_pass = password
