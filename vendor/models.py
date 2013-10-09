from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User 

class Vendor(models.Model):
  user = models.ForeignKey(User, unique=True)
  vendorname = models.CharField(max_length=64)
  profile = models.TextField()
  active = models.BooleanField(default=False)
  pubkey = models.TextField()

  @classmethod
  def is_vendor(cls, user):
    return (cls.objects.filter(user=user,active=True).count() > 0)

class VendorForm(ModelForm):
  class Meta:
    model = Vendor
    fields = ['vendorname', 'profile']

