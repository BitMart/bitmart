from django.shortcuts import render

from listing.models import Listing
from vendor.models import Vendor

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
