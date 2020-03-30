import MySQLdb
from numpy.random import randint
import time
start_time = time.time()

try:
    conn=MySQLdb.connect('localhost','root','','event')
    if conn:
        print("Successfully Connected")
except:
    print("Connection Failed")

c=conn.cursor()
sql = "CREATE TABLE IF NOT EXISTS FIFA (scores int)"
c.execute(sql)
for i in range(1,100000):
    r=randint(low=10,high=30)
    c.execute('INSERT INTO FIFA VALUES(8)')

#c.execute("SELECT * FROM FIFA")
#print("After Inserting \n",c.fetchall())
print("--- %s seconds --- to save 100000 recores in Database" % (time.time() - start_time))
