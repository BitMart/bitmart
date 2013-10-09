from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',         'bitmart.views.index'), 
    url(r'^account/',  include('account.urls')),
    url(r'^wallet/',   include('wallet.urls')),
    url(r'^listing/',  include('listing.urls')),
    url(r'^vendor/',   include('vendor.urls')),

    url(r'^admin/',    include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
