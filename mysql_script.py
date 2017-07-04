#!/usr/bin/python

import MySQLdb

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
db.close()
