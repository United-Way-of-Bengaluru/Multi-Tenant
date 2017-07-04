# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import MySQLdb

# Create your models here.
class Tenants(models.Model):
	name = models.CharField(max_length=200)
	encryption_key = models.CharField(max_length=200)

	def save(self, *args, **kwargs):
		print ("Line 12, Save Tenants", self.name)
		
		# Open database connection
		db = MySQLdb.connect("localhost","root","admin", "multi_tenant")

		# prepare a cursor object using cursor() method
		cursor = db.cursor()

		# execute SQL query using execute() method.
		cursor.execute("SELECT VERSION()")


		print "Creating Database ...";
		dbname = "tenant_%s" % self.name.lower()

		sql = 'CREATE DATABASE IF NOT EXISTS %s' % dbname
		cursor.execute(sql)

		print "Database Created successfully"

		db1 = MySQLdb.connect("localhost","root","admin", dbname)
		cursor1 = db1.cursor()

		self.exec_sql_file(cursor1, 'multi_tenant.sql')

		# disconnect from server
		db.close()

		super(Tenants, self).save(*args, **kwargs)

	def exec_sql_file(self, cursor, sql_file):
	    print "\n[INFO] Executing SQL script file: '%s'" % (sql_file)
	    statement = ""

	    for line in open(sql_file):
	        if line.strip().startswith('--'): # ignore sql comment lines
	            continue
	        if not line.strip().endswith(';'):  # keep appending lines that don't end in ';'
	            statement = statement + line
	        else:  # when you get a line ending in ';' then exec statement and reset for next statement
	            statement = statement + line
	            #print "\n\n[DEBUG] Executing SQL statement:\n%s" % (statement)
	            try:
	                cursor.execute(statement)
	            except (OperationalError, ProgrammingError) as e:
	                print "\n[WARN] MySQLError during execute statement \n\tArgs: '%s'" % (str(e.args))

	            statement = ""
	
