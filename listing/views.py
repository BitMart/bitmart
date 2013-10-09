from django.shortcuts import render
from listing.models import Category

def index(request, catid=0):
  cats = Category.objects.filter(parent=None)

  return render(request, 'listing/index.html', {
    'categories': cats,
    'category': int(catid)
  })

def view(request):
  return render(request, 'listing/view.html', {})

def create(request):
  return render(request, 'listing/create.html', {})

def purchase(request):
  return render(request, 'listing/purchase.html', {})
