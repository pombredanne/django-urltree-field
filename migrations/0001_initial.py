# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'URLTree'
        db.create_table('urltree_urltree', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('domain', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('urltree', ['URLTree'])

        # Adding model 'URLNode'
        db.create_table('urltree_urlnode', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('urltree', self.gf('django.db.models.fields.related.ForeignKey')(related_name='nodes', to=orm['urltree.URLTree'])),
            ('url', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['urltree.URLNode'])),
            ('checked', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('info', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('urltree', ['URLNode'])


    def backwards(self, orm):
        
        # Deleting model 'URLTree'
        db.delete_table('urltree_urltree')

        # Deleting model 'URLNode'
        db.delete_table('urltree_urlnode')


    models = {
        'urltree.urlnode': {
            'Meta': {'object_name': 'URLNode'},
            'checked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['urltree.URLNode']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'urltree': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'nodes'", 'to': "orm['urltree.URLTree']"})
        },
        'urltree.urltree': {
            'Meta': {'ordering': "('-created_at',)", 'object_name': 'URLTree'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'domain': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['urltree']
