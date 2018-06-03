from django.db import models
from django.utils import timezone

from hubs.models import Hubspot


class AuthUser(models.Model):
    user_name = models.CharField(max_length=200, blank=True)
    user_pass = models.CharField(max_length=200, blank=False, default="")
    user_email = models.EmailField(max_length=200, blank=False, default="",
                                   primary_key=True)

    def __str__(self):
        return self.user_name if self.user_name != "" else self.user_email


class Checkin(models.Model):
    checkin_user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    checkin_hub = models.ForeignKey(Hubspot, on_delete=models.CASCADE)
    checkin_active = models.BooleanField(default=True)
    checkin_datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%s %s" % (self.checkin_user, self.checkin_hub)
