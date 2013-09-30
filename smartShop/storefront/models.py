from django.db import models
from django.forms import ModelForm

# Create your models here.

class Store(models.Model):
    store_name = models.CharField(max_length=255)
    store_address = models.CharField(max_length=255)
    store_phone = models.CharField(max_length=255)
    store_website = models.CharField(max_length=255)
    store_email = models.EmailField(max_length=100)
    store_hours = models.CharField(max_length=255)
    store_coverpic = models.FileField(upload_to='store/cover/',null=True,blank=True)

    def __unicode__(self):
        return self.store_name   
        
class StoreAdmin(models.Model):
    admin_email = models.CharField(max_length=255)
    admin_password = models.CharField(max_length=255)
    admin_storeid = models.ForeignKey(Store)

    def __unicode__(self):
        return self.admin_email;

class ProductAlbum(models.Model):
    album_name = models.CharField(max_length=255)
    album_store_name = models.ForeignKey(Store)
    album_product_number = models.IntegerField(max_length=255)
    album_cover = models.FileField(upload_to='album/cover/',null=True,blank=True)

    def __unicode__(self):
        return self.album_name
 
class ProductDetails(models.Model):
    STOCK_OPTIONS = (
        ('I','In Stock'),
        ('O','Out of Stock'),
        ('S','Soon in Stock')
    )
    product_name = models.CharField(max_length=255)
    product_image = models.FileField(upload_to='product/main/',null=True,blank=True)
    product_price =  models.IntegerField(max_length=255)
    product_inStock = models.CharField(max_length=2,choices=STOCK_OPTIONS)
    product_album_name = models.ForeignKey(ProductAlbum)

    def __unicode__(self):
        return self.product_name
