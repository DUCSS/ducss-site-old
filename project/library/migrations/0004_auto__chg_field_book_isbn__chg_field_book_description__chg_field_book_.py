# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Book.isbn'
        db.alter_column('library_book', 'isbn', self.gf('django.db.models.fields.CharField')(max_length=13, null=True))

        # Changing field 'Book.description'
        db.alter_column('library_book', 'description', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Book.isbn13'
        db.alter_column('library_book', 'isbn13', self.gf('django.db.models.fields.CharField')(max_length=13, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Book.isbn'
        raise RuntimeError("Cannot reverse this migration. 'Book.isbn' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Book.description'
        raise RuntimeError("Cannot reverse this migration. 'Book.description' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Book.isbn13'
        raise RuntimeError("Cannot reverse this migration. 'Book.isbn13' and its values cannot be restored.")

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
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '13', 'null': 'True', 'blank': 'True'}),
            'isbn13': ('django.db.models.fields.CharField', [], {'max_length': '13', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'max_length': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'year_published': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'library.reservation': {
            'Meta': {'object_name': 'Reservation'},
            'book_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['library.Book']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 8, 31, 0, 0)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member_name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['library']