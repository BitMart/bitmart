from django.conf.urls import patterns, url

urlpatterns = patterns('listing.views', 
    url(r'(\d+)?$',         'index'),
    url(r'view/(\d+)$',     'view'),
    url(r'create$',         'create'),
    url(r'purchase/(\d+)$', 'purchase'),
)
