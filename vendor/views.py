from django.shortcuts import render
from listing.models import *

def index(req):
  return render(req, 'vendor/index.html', {})
