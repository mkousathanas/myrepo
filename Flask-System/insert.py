import sqlite3
#conn = sqlite3.connect('database.db')
"""Για την έναρξη της σύνδεσης με τη βάση δεδομένων"""
with sqlite3.connect("database.db") as con:cur = con.cursor()
print ("Πετυχημένη σύνδεση με τη βάση δεδομένων");
cur.execute("INSERT INTO users (name,addr,city,pin)VALUES ('abc1','aa 20','aaa1','1234a')")

con.commit()
msg = "Η εγγραφή προστέθηκε με επιτυχία"
print (msg)
con.close()