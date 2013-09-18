from django.db import models

# Create your models here.

class Store(models.Model):
    store_name = models.CharField(max_length=255)
    store_address = models.CharField(max_length=255)
    store_phone = models.CharField(max_length=255)
    store_website = models.CharField(max_length=255)
    store_email = models.CharField(max_length=255)
    store_hours = models.CharField(max_length=255)   
        
class StoreAdmin(models.Model):
    admin_email = models.CharField(max_length=255)
    admin_password = models.CharField(max_length=255)
    admin_storeid = models.ForeignKey(Store)

class ProductAlbum(models.Model):
    album_name = models.CharField(max_length=255)
    album_store_name = models.ForeignKey(Store)
    album_product_number = models.IntegerField(max_length=255)
    album_photograph = models.CharField(max_length=255)
 
class ProductDetails(models.Model):
    product_name = models.CharField(max_length=255)
    product_image = models.CharField(max_length=255)
    product_price =  models.IntegerField(max_length=255)
    product_inStock = models.BooleanField()
    product_album_name = models.ForeignKey(ProductAlbum)

