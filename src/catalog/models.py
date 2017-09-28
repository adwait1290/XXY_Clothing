from __future__ import unicode_literals
import os
from uuid import uuid4

from django.core.urlresolvers import reverse

from django.db import models

# Create your models here.



class Category(models.Model):
	name = models.CharField('Name', max_length=100)
	slug = models.CharField('Identifier', max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	class Meta:
		verbose_name="Category"
		verbose_name_plural="Categories"
		ordering = ['name']
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('catolog:category', kwargs={'slug': self.slug})
def path_and_rename(instance, filename):
    upload_to = '/images/products/main/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    name = os.path.join(upload_to, filename)
    return os.path.join(upload_to, filename)

class Product(models.Model):
	name = models.CharField('Name', max_length=100)
	slug = models.CharField('Identifier', max_length=100)
	category = models.ForeignKey('Category', verbose_name="Category")
	description = models.TextField('Description', blank=True)
	image = models.ImageField(upload_to='img',max_length=100, null=True)
	price = models.DecimalField('Price', decimal_places=2, max_digits=8)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	class Meta:
		verbose_name="Product"
		verbose_name_plural="Products"
		ordering = ['name']
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('catalog:product', kwargs={'slug': self.slug})
	def get_img_url(self):
		return path_and_rename(name)