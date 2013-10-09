from django.conf.urls import patterns, url

urlpatterns = patterns('vendor.views', 
    url(r'register$', 'register'),
    url(r'search$',   'search'),
    url(r'$',         'index'),
)
