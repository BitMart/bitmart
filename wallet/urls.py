from django.conf.urls import patterns, url

urlpatterns = patterns('wallet.views', 
    url(r'^$', 'index'),
    url(r'^create$', 'create'),
    url(r'^send$', 'send'),
)
