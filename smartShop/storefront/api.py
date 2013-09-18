from tastypie.resources import ModelResource
from storefront.models import Store,ProductAlbum,ProductDetails
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie import fields








class StoreResource(ModelResource):
    class Meta:
        print "didnt get a variable"
    
        queryset =Store.objects.all()
        for i in queryset:
            print i.__dict__
    
        #excludes = ['id','meta']
        resource_name = 'store'
        include_resource_uri = False
        filtering = {
            #"id": ALL,
            "id":('exact',),
        }



class AlbumResource(ModelResource):
    storeId = fields.ForeignKey(StoreResource,'album_store_name')
    class Meta:
        queryset = ProductAlbum.objects.all()
        for i in queryset:
            print i.__dict__
        resource_name = 'album'
        include_resource_uri = False
        filtering = {
            'storeId' : ALL,
        }
        print "here we go now"
        for i in queryset:
            print i.__dict__
        

class ProductResource(ModelResource):
    albumId = fields.ForeignKey(AlbumResource,'product_album_name')
    class Meta:
        queryset = ProductDetails.objects.all()
        for i in queryset:
            print i.__dict__
        resource_name = 'products'
        include_resource_uri = False
        filtering = {
            'albumId' : ALL,
        }
        print "here we go now"
        for i in queryset:
            print i.__dict__
 

        
        #def dispatch_list(self, request, **kwargs):
        #    print "got here"
        #    body_filters = parse_xml_get_data(request)
        #    print body_filters
        #    kwargs.update(body_filters)
        #    return super(MyResource, self).dispatch_list(request, **kwargs)
