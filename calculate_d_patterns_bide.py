import os
import MySQLdb

class DP(object):
	def __init__(self):
		pass

	def compose(self, dp, p):
		for k,v in p.iteritems():
			try:
				dp[k] += v
			except:
				dp[k] = v
		return dp

	def d_patterns(self, sp):
			dp = {}
			for pat in sp:
				p = {}
				for t in pat:
					p[t] = 1
				dp = self.compose(dp, p)
			return dp

path = "/home/om/Development/TextMining/data/"

connection = MySQLdb.connect('localhost', 'root', 'root', 'mining')
cursor = connection.cursor()

dirlist = [d for d in os.listdir(path) if '.txt' in d ]
dp = DP()

for d in dirlist:
	os.system("java -jar spmf.jar run BIDE+_with_strings data/"+d+" temp_output 20% > temp")
	f = open('temp_output', 'r')
	ft = open('temp' , 'r')
	sp = []
	while True:
		l = f.readline()
		if not l:
			break
		l = l.split('SUP')[0].replace('-1 ', '')
		sp.append(l.split())
	print sp
	ft.readline()
	exec_time = ft.readline().split()[3]
	dpps = str(dp.d_patterns(sp))
	id = d.split('.')[0]
	query = 'Update data set `dp` = \''+dpps.replace('\'', '"')+'\' where id = '+id
	cursor.execute(query)
	