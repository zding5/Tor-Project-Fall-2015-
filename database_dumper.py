import MySQLdb as dbapi
import sys
import csv

def dump(ip,user,pw,db,table):
	dbServer='localhost'
	dbPass=''
	# dbSchema='dbTest'
	dbUser='root'

	# dbQuery='SELECT * FROM tor_oct;'
	dbQuery='SELECT * FROM %s' % table

	# db=dbapi.connect(host=dbServer,user=dbUser,passwd=dbPass)
	# db = dbapi.connect("127.0.0.1", "root", "", "Tor")
	db=dbapi.connect(ip,user,pw,db)
	cur=db.cursor()
	cur.execute(dbQuery)
	result=cur.fetchall()

	c = csv.writer(open("tor.csv","wb"))
	for row in result:
	    c.writerow(row)

if __name__ == '__main__':
	dump(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])