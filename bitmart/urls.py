from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bitmart.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'bitmart.views.index'),
    
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.backends.default.urls')),
    (r'^account/', 'account.views.index'),

    url(r'wallet/$', 'wallet.views.index'),
    url(r'wallet/create$', 'wallet.views.create'),
    url(r'wallet/send$', 'wallet.views.send'),

    url(r'listing/(\d+)?$', 'listing.views.index'),
    url(r'listing/view/(\d+)/$', 'listing.views.view'),
    url(r'listing/create/$', 'listing.views.create'),
    url(r'listing/purchase/(\d+)/$', 'listing.views.purchase'),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
