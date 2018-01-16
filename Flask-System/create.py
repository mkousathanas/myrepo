import sqlite3
"""Για την έναρξη της σύνδεσης με τη βάση δεδομένων"""
conn = sqlite3.connect('database.db')
print "Πετυχημένη σύνδεση με τη βάση δεδομένων";

conn.execute('CREATE TABLE users (name TEXT, addr TEXT, city TEXT, pin TEXT)')
print "Ο πίνακας δημιουργήθηκε με επιτυχία";
conn.close()