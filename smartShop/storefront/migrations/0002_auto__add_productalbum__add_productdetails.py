# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProductAlbum'
        db.create_table(u'storefront_productalbum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('album_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('album_store_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['storefront.Store'])),
            ('album_product_number', self.gf('django.db.models.fields.IntegerField')(max_length=255)),
            ('album_photograph', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'storefront', ['ProductAlbum'])

        # Adding model 'ProductDetails'
        db.create_table(u'storefront_productdetails', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('product_image', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('product_price', self.gf('django.db.models.fields.IntegerField')(max_length=255)),
            ('product_inStock', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'storefront', ['ProductDetails'])


    def backwards(self, orm):
        # Deleting model 'ProductAlbum'
        db.delete_table(u'storefront_productalbum')

        # Deleting model 'ProductDetails'
        db.delete_table(u'storefront_productdetails')


    models = {
        u'storefront.productalbum': {
            'Meta': {'object_name': 'ProductAlbum'},
            'album_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'album_photograph': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'album_product_number': ('django.db.models.fields.IntegerField', [], {'max_length': '255'}),
            'album_store_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['storefront.Store']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'storefront.productdetails': {
            'Meta': {'object_name': 'ProductDetails'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product_image': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'product_inStock': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'product_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'product_price': ('django.db.models.fields.IntegerField', [], {'max_length': '255'})
        },
        u'storefront.store': {
            'Meta': {'object_name': 'Store'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'store_address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'store_email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'store_hours': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'store_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'store_phone': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'store_website': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'storefront.storeadmin': {
            'Meta': {'object_name': 'StoreAdmin'},
            'admin_email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'admin_password': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'admin_storeid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['storefront.Store']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['storefront']