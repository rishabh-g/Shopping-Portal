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

