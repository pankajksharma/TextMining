import MySQLdb
import json

f = open('topics', 'r')
topics = {}
while True:
	t = f.readline()
	if not t:
		break
	t = t.split()
	try:
		topics[t[1]].append(t[0])
	except:
		topics[t[1]] = [t[0]]

f.close()

connection = MySQLdb.connect('localhost', 'root', 'root', 'mining')
cursor = connection.cursor()
cursor2 = connection.cursor()
query = "select id from data"
cursor.execute(query)
cursor.scroll(0, 'absolute')
while True:
	c = cursor.fetchone()
	if not c:
		break
	id = str(c[0])
	rel_topics = str(json.dumps(topics[id]))
	query = "update `data` set type=%s where id=%s"%(rel_topics, id)
	cursor2.execute(query)
	connection.commit()