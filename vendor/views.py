from django.shortcuts import render
from listing.models import *

def index(req):
  return render(req, 'vendor/index.html', {})

def register(req):
  return render(req, 'vendor/register.html', {})

def search(req):
  return render(req, 'vendor/search.html', {})

