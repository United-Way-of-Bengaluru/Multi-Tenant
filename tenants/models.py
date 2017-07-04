# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import MySQLdb

# Create your models here.
class Tenants(models.Model):
	name = models.CharField(max_length=200)
	encryption_key = models.CharField(max_length=200)

	def save(self, *args, **kwargs):
		print ("Line 12, Save Tenants", args, kwargs)
		'''
		# Open database connection
		db = MySQLdb.connect("localhost","root","admin", "multi_tenant")

		# prepare a cursor object using cursor() method
		cursor = db.cursor()

		# execute SQL query using execute() method.
		cursor.execute("SELECT VERSION()")


		print "Creating Database ...";

		sql = 'CREATE DATABASE IF NOT EXISTS mydata1'
		cursor.execute(sql)

		print "Database Created successfully"

		# disconnect from server
		db.close()'''

		super(Tenants, self).save(*args, **kwargs)
	
