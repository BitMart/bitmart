from django.shortcuts import render
from listing.models import *

def index(request, catid=0):
  if (catid == None): catid = 0 
  selected = Category.objects.filter(id=catid)
  if (selected.count()>0 and selected.first().parent != None):
    cats = selected
  else:
    cats = Category.objects.filter(parent=None)

  return render(request, 'listing/index.html', {
    'categories': cats,
    'category': int(catid)
  })

def view(request):
  return render(request, 'listing/view.html', {})

def create(request):
  form = ListingForm()
  return render(request, 'listing/create.html', {
    'form': form
  })

def purchase(request):
  return render(request, 'listing/purchase.html', {})
