# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Author'
        db.create_table('library_author', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('library', ['Author'])

        # Adding model 'Book'
        db.create_table('library_book', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('isbn', self.gf('django.db.models.fields.CharField')(max_length=13)),
            ('isbn13', self.gf('django.db.models.fields.CharField')(max_length=13)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('library', ['Book'])

        # Adding M2M table for field authors on 'Book'
        m2m_table_name = db.shorten_name('library_book_authors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm['library.book'], null=False)),
            ('author', models.ForeignKey(orm['library.author'], null=False))
        ))
        db.create_unique(m2m_table_name, ['book_id', 'author_id'])

        # Adding model 'Reservation'
        db.create_table('library_reservation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('book_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['library.Book'])),
            ('member_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('library', ['Reservation'])

        # Adding model 'Status'
        db.create_table('library_status', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('book_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['library.Book'])),
            ('status', self.gf('django.db.models.fields.TextField')()),
            ('last_member', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('library', ['Status'])


    def backwards(self, orm):
        # Deleting model 'Author'
        db.delete_table('library_author')

        # Deleting model 'Book'
        db.delete_table('library_book')

        # Removing M2M table for field authors on 'Book'
        db.delete_table(db.shorten_name('library_book_authors'))

        # Deleting model 'Reservation'
        db.delete_table('library_reservation')

        # Deleting model 'Status'
        db.delete_table('library_status')


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
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'library.reservation': {
            'Meta': {'object_name': 'Reservation'},
            'book_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['library.Book']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member_name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'library.status': {
            'Meta': {'object_name': 'Status'},
            'book_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['library.Book']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_member': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'status': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['library']