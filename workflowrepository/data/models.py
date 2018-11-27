# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django
from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=128,unique=True, blank=False)
	slug = models.SlugField(unique=True)
	created = models.DateField(auto_now=True)
	tooltip = models.CharField(max_length=128)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name

class Workflow(models.Model):
	name = models.CharField(max_length=128, unique=True, blank=False)
	slug = models.SlugField(unique=True)
	description = models.CharField(max_length=512, default="")
	views = models.IntegerField(default=0)
	downloads = models.IntegerField(default=0)
	versionInit = models.CharField(max_length=512)
	category = models.ManyToManyField(Category, blank=False)
	client_ip = models.GenericIPAddressField(default='192.168.0.1')
	keywords = models.CharField(max_length=256, default = "")
	json = models.TextField(max_length=512)
	created = models.DateField(auto_now=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Workflow, self).save(*args, **kwargs)

	def __str__(self): # For Python 2, use __unicode__ too
		return self.name

	def __unicode__(self):
	        return self.name
