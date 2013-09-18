from django.contrib import admin
#from smartShop.storefront import *
from storefront.models import Store,StoreAdmin,ProductAlbum,ProductDetails

admin.site.register(Store)
admin.site.register(StoreAdmin)
admin.site.register(ProductAlbum)
admin.site.register(ProductDetails)
