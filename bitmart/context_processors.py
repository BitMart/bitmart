from django.conf import settings

def path(request):
  if request.path.startswith('/vendor'):
    at = 'vendor'
  elif request.path.startswith('/listing'):
    at = 'listing'
  elif request.path.startswith('/account'):
    at = 'account'
  elif request.path.startswith('/wallet'):
    at = 'account'
  else:
    at = 'home'
  return {'pagename': at}

def site(request):
    return {'SITE_URL': settings.SITE_URL}
