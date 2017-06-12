# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Featured'
        db.create_table(u'products_featured', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('date_start', self.gf('django.db.models.fields.DateField')()),
            ('date_end', self.gf('django.db.models.fields.DateField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('default', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('jumbo_text', self.gf('django.db.models.fields.CharField')(max_length=3000, null=True, blank=True)),
        ))
        db.send_create_signal(u'products', ['Featured'])

        # Adding M2M table for field products on 'Featured'
        m2m_table_name = db.shorten_name(u'products_featured_products')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('featured', models.ForeignKey(orm[u'products.featured'], null=False)),
            ('product', models.ForeignKey(orm[u'products.product'], null=False))
        ))
        db.create_unique(m2m_table_name, ['featured_id', 'product_id'])

        # Deleting field 'CategoryImage.description'
        db.delete_column(u'products_categoryimage', 'description')

        # Deleting field 'CategoryImage.slug'
        db.delete_column(u'products_categoryimage', 'slug')

        # Adding field 'CategoryImage.image'
        db.add_column(u'products_categoryimage', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(default=2, max_length=100),
                      keep_default=False)

        # Adding field 'CategoryImage.featured_image'
        db.add_column(u'products_categoryimage', 'featured_image',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'CategoryImage.title'
        db.alter_column(u'products_categoryimage', 'title', self.gf('django.db.models.fields.CharField')(max_length=120, null=True))
        # Removing M2M table for field product on 'Category'
        db.delete_table(db.shorten_name(u'products_category_product'))

        # Adding M2M table for field products on 'Category'
        m2m_table_name = db.shorten_name(u'products_category_products')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('category', models.ForeignKey(orm[u'products.category'], null=False)),
            ('product', models.ForeignKey(orm[u'products.product'], null=False))
        ))
        db.create_unique(m2m_table_name, ['category_id', 'product_id'])


    def backwards(self, orm):
        # Deleting model 'Featured'
        db.delete_table(u'products_featured')

        # Removing M2M table for field products on 'Featured'
        db.delete_table(db.shorten_name(u'products_featured_products'))

        # Adding field 'CategoryImage.description'
        db.add_column(u'products_categoryimage', 'description',
                      self.gf('django.db.models.fields.CharField')(default=2, max_length=500),
                      keep_default=False)

        # Adding field 'CategoryImage.slug'
        db.add_column(u'products_categoryimage', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default=1, max_length=50),
                      keep_default=False)

        # Deleting field 'CategoryImage.image'
        db.delete_column(u'products_categoryimage', 'image')

        # Deleting field 'CategoryImage.featured_image'
        db.delete_column(u'products_categoryimage', 'featured_image')


        # Changing field 'CategoryImage.title'
        db.alter_column(u'products_categoryimage', 'title', self.gf('django.db.models.fields.CharField')(default=2, max_length=120))
        # Adding M2M table for field product on 'Category'
        m2m_table_name = db.shorten_name(u'products_category_product')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('category', models.ForeignKey(orm[u'products.category'], null=False)),
            ('product', models.ForeignKey(orm[u'products.product'], null=False))
        ))
        db.create_unique(m2m_table_name, ['category_id', 'product_id'])

        # Removing M2M table for field products on 'Category'
        db.delete_table(db.shorten_name(u'products_category_products'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'products.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['products.Product']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'products.categoryimage': {
            'Meta': {'object_name': 'CategoryImage'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.Category']"}),
            'featured_image': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'products.featured': {
            'Meta': {'object_name': 'Featured'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'date_end': ('django.db.models.fields.DateField', [], {}),
            'date_start': ('django.db.models.fields.DateField', [], {}),
            'default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jumbo_text': ('django.db.models.fields.CharField', [], {'max_length': '3000', 'null': 'True', 'blank': 'True'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['products.Product']", 'symmetrical': 'False', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'products.product': {
            'Meta': {'ordering': "[u'-order']", 'object_name': 'Product'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'download': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'}),
            'sale_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '180'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'products.productimage': {
            'Meta': {'object_name': 'ProductImage'},
            'featured_image': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.Product']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'products.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.Product']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['products']