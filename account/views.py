from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from account.models import Account
from listing.models import Listing
from vendor.models import Vendor
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as _logout
from django.contrib.auth import login as _login

def index(request):
  isvendor = Vendor.is_vendor(request.user)
  if isvendor:
    listings = Listing.objects.filter(vendor=request.user)
  else:
    listings = []

  return render(request, 'account/index.html', {
    'username': request.user.username,
    'isvendor': isvendor,
    'listings': listings
  })

def login(req):
  msg = ''
  if req.method == 'POST':
    u = authenticate(username=req.POST['username'],password=req.POST['password'])
    if u != None:
      _login(req,u)
      return HttpResponseRedirect('/account/')
    else:
      msg = 'Invalid credentials'
  return render(req, 'account/login.html', {'msg':msg})

def logout(req):
  _logout(req)
  return HttpResponseRedirect('/')

def register(req):
  errors = {}
  if req.method == 'POST':
    d = req.POST
    un = d['username']
    pi = d['pin']
    p1 = d['password1']
    p2 = d['password2']

    valid = True

    if User.objects.filter(username=un).count() > 0:
      valid = False
      errors['username'] = 'Must be unique.'

    if len(pi) < 4 or len(pi) > 6:
      valid = False
      errors['pin'] = 'Must be between 4 and 6 characters.'

    if p1 != p2:
      valid = False
      m = 'Passwords must match.'
      errors['password1'] = m
      errors['password2'] = m

    if valid:
      new = User.objects.create_user(un,"%s@%s.io"%(un,un),p1)
      new.save()
      acc = Account(user=new,pin=pi)
      acc.save()

      user = authenticate(username=un, password=p1)
      if user != None:
        _login(req,user)
        return HttpResponseRedirect('/account/')
      else:
        return HttpResponseRedirect('/')
      
  
  return render(req, 'account/register.html', {
    'errors': errors   
  })
