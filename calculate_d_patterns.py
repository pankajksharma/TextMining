from gapbide import Gapbide
import MySQLdb
import json

class DP(object):
	def __init__(self, min_sup):
		self.min_sup = min_sup

	def compose(self, dp, p):
		for k,v in p.iteritems():
			try:
				dp[k] += v
			except:
				dp[k] = v
		return dp

	def d_patterns(self, doc):
			if len(doc) != 1:
				sp = Gapbide(doc, self.min_sup*len(doc), 0, 3).run()
			else:
				sp = doc[0]
			dp = {}
			for pat in sp:
				p = {}
				for t in pat:
					p[t] = 1
				dp = self.compose(dp, p)
			return dp

p=DP(0.5)
print p.d_patterns([[1,2,3,4],[2,4,5,3],[3,6,1],[5,1,2,7,3]])
# print p.get_terms_support()

connection = MySQLdb.connect('localhost', 'root', 'root', 'mining')
cursor = connection.cursor()
cursor2 = connection.cursor()
query = "select id,data from data"
cursor.execute(query)
cursor.scroll(0, 'absolute')
dp = DP(0.3)
while True:
	c = cursor.fetchone()
	if not c:
		break
	data = c[-1].replace('\'','"')
	dps = dp.d_patterns(json.loads(data))
	query = "update data set dp = '%s' where id = %s" %(json.dumps(dps), str(c[0]))
	cursor2.execute(query)
	connection.commit()