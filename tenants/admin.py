# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Tenants

# Register your models here.
class Tenants_admin(admin.ModelAdmin):
	list_display = ('name', 'encryption_key')
	'''def save_model(self, request, obj, form, change):
		print "Line 11, Admin Tenant"
        super(Tenants).save_model(request, obj, form, change)'''

admin.site.register(Tenants, Tenants_admin)
