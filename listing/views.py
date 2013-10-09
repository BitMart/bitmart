from django.shortcuts import render
from listing.models import Category, Listing
from django.forms import ModelForm

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

class ListingForm(ModelForm):
  class Meta:
    model = Listing
    fields = ['title','description','cost','image']

def view(request):
  return render(request, 'listing/view.html', {})

def create(request):
  form = ListingForm()
  return render(request, 'listing/create.html', {
    'form': form
  })

def purchase(request):
  return render(request, 'listing/purchase.html', {})
