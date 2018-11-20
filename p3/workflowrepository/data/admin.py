# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from data.models import Category, Workflow

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug')

class WorkflowAdmin(admin.ModelAdmin):
	list_display = ( 'name', 'slug', 'views', 'downloads', 'client_ip', 'created')

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Workflow, WorkflowAdmin)
