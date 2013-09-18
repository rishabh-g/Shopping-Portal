from django.conf.urls import patterns, include, url
from storefront import views
from tastypie.api import Api
from storefront.api import StoreResource,AlbumResource,ProductResource 
store_resource = StoreResource() 

v1_api = Api(api_name='v1')
v1_api.register(StoreResource())
v1_api.register(AlbumResource())
v1_api.register(ProductResource())


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

    url(r'^$', views.index, name='index'),
    url(r'^storefront/',include('storefront.urls',namespace="storefront")),
    url(r'^store/',include(v1_api.urls)),
    #url(r'^$', 'smartShop.views.home', name='home'),
    # url(r'^smartShop/', include('smartShop.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
