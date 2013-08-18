from django.conf.urls import patterns, include, url
from storefront import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'storefront.views.home', name='home'),
    url(r'login$', 'storefront.views.login', name='login'),
    url(r'register$', 'storefront.views.register', name='register'),
    # url(r'^smartShop/', include('smartShop.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
