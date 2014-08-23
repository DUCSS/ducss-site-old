# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Reservation.email'
        db.add_column('library_reservation', 'email',
                      self.gf('django.db.models.fields.EmailField')(default='email@email.com', max_length=75),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Reservation.email'
        db.delete_column('library_reservation', 'email')


    models = {
        'library.author': {
            'Meta': {'object_name': 'Author'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'library.book': {
            'Meta': {'object_name': 'Book'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['library.Author']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'isbn13': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'status': ('django.db.models.fields.TextField', [], {'default': "'In'"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'year_published': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True'})
        },
        'library.reservation': {
            'Meta': {'object_name': 'Reservation'},
            'book_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['library.Book']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member_name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['library']