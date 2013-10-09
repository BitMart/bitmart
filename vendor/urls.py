from django.conf.urls import patterns, url

urlpatterns = patterns('vendor.views', 
    url(r'$',         'index'),
    url(r'register$', 'register'),
    url(r'search$',   'search')
)
