from django.db import models
from django.contrib.auth.models import User
class Account(models.Model):
  user = models.ForeignKey(User, unique=True)
  pin = models.CharField(max_length=6)
