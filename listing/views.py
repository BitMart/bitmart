from django.shortcuts import render
from listing.models import *

def index(request, slug=''):
  selected = Category.objects.filter(slug=slug)
  if (selected.count()>0 and selected.first().parent != None):
    cats = selected
  else:
    cats = Category.objects.filter(parent=None)

  return render(request, 'listing/index.html', {
    'categories': cats,
    'category': slug
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
