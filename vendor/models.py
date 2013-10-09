from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User 
from django.contrib import admin

class Vendor(models.Model):
  user = models.ForeignKey(User, unique=True)
  active = models.BooleanField(default=False)

  vendorname = models.CharField(max_length=64)
  profile = models.TextField()
  pubkey = models.TextField()

  @classmethod
  def is_vendor(cls, user):
    return (cls.objects.filter(user=user,active=True).count() > 0)
  def __unicode__(self): return self.vendorname

class VendorForm(ModelForm):
  class Meta:
    model = Vendor
    fields = ['vendorname', 'profile', 'pubkey']

admin.site.register(Vendor)
