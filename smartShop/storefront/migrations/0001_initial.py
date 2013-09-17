# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Store'
        db.create_table(u'storefront_store', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('store_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('store_address', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('store_phone', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('store_website', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('store_email', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('store_hours', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'storefront', ['Store'])

        # Adding model 'StoreAdmin'
        db.create_table(u'storefront_storeadmin', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('admin_email', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('admin_password', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('admin_storeid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['storefront.Store'])),
        ))
        db.send_create_signal(u'storefront', ['StoreAdmin'])


    def backwards(self, orm):
        # Deleting model 'Store'
        db.delete_table(u'storefront_store')

        # Deleting model 'StoreAdmin'
        db.delete_table(u'storefront_storeadmin')


    models = {
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