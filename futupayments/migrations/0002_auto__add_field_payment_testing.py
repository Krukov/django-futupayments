# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Payment.testing'
        db.add_column(u'futupayments_payment', 'testing',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Payment.testing'
        db.delete_column(u'futupayments_payment', 'testing')


    models = {
        u'futupayments.payment': {
            'Meta': {'ordering': "('-creation_datetime',)", 'unique_together': "(('state', 'transaction_id'),)", 'object_name': 'Payment'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'creation_datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'meta': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'order_id': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'testing': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'transaction_id': ('django.db.models.fields.BigIntegerField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['futupayments']