from tastypie.resources import ModelResource
from storefront.models import Store

class StoreResource(ModelResource):
    class Meta:
        queryset =Store.objects.all()
        excludes = ['id','resource_uri']
        resource_name = 'store'
        

