from django.db import models
from django.forms import ModelForm

class Vendor(models.Model):
  user = models.ForeignKey(User, unique=True)
  vendorname = models.CharField(max_length=64)
  profile = models.TextField()

class VendorForm(ModelForm):
  class Meta:
    model = Vendor
    fields = ['vendorname', 'profile']

