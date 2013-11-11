import MySQLdb
import json

connection = MySQLdb.connect('localhost', 'root', 'root', 'mining')
cursor = connection.cursor()
query = "select * from data where type='pos'"
cursor.execute(query)
cursor.scroll(0, 'absolute')
path = "/home/om/Development/TextMining/data/"
while True:
	c = cursor.fetchone()
	if not c:
		break
	data = c[-1].replace('\'','"')
	arr = json.loads(data)
	f = open(path+str(c[0])+".txt", "w")
	for a in arr:
		for ai in a:
			f.write(ai+' -1 ')
		f.write('-2\n')
	f.close()