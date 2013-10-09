from django.shortcuts import render
from vendor.models import VendorForm, Vendor
from django.http import HttpResponseRedirect

def index(req):
  return render(req, 'vendor/index.html', {})

def register(req):
  if req.method == 'POST':
    form = VendorForm(req.POST)
    if form.is_valid():
      new = Vendor(
          user       = req.user,
          vendorname = form.cleaned_data['vendorname'],
          profile    = form.cleaned_data['profile'],
          pubkey     = form.cleaned_data['pubkey']
      )
      new.save()

      return HttpResponseRedirect('/account/thanks')
  else:
    form = VendorForm()

  return render(req, 'vendor/register.html', {'form':form})

def search(req):
  return render(req, 'vendor/search.html', {})

