from django.conf.urls import patterns, include, url
from django.contrib import admin
from storefront import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'storefront.views.home', name='home'),
    url(r'login$', 'storefront.views.login', name='login'),
    url(r'register$', 'storefront.views.register', name='register'),
    url(r'product_details$', 'storefront.views.product_details', name='product_details'),
    url(r'imagehandler$', 'storefront.views.imagehandler', name='imagehandler'),
    url(r'individual_details$', 'storefront.views.individual_details', name='individual_details'),


    # url(r'^smartShop/', include('smartShop.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
