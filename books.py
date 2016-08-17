#!/usr/bin/env python

import sqlite3 as db

conn = db.connect('test.db')
cursor = conn.cursor()

print "Content-Type: text/html\n"
print "<html><head><title>Books</title></head>"
print "<body>"
print "<h1>Books</h1>"
print "<ul>"

cursor.execute("SELECT name FROM books ORDER BY pub_date DESC LIMIT 3")

for row in cursor.fetchall():
    print "<li>%s</li>" % row[0]

print "</ul>"
print "</body></html>"

conn.close()
