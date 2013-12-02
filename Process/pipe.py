import json
class IPE(object):
	"""docstring for IPE"""
	def __init__(self, connection, coeff, term_support):
		self.coeff = coeff
		self.connection = connection
		self.term_support = term_support
		
	def threshold(self):
		cursor = self.connection.cursor()
		query = "select dp from `data` where dp != NULL"
		cursor.execute(query)
		threshold = 1
		cursor.scroll(0, 'absolute')
		while True:
			c = cursor.fetchone()
			if not c:
				break
			ndp = json.loads(c[0].replace('\'','"'))
			ts = 0.0
			for k in ndp.keys():
				ts += self.term_support[k]
			if ts < threshold:
				threshold = ts
			return threshold
			
	def weight(self, paras):
		weight = 0.0
		for para in paras:
			for term in para:
				weight += self.term_support[term]
		return weight

	def noise_neg_docs(self):
		threshold = self.threshold()
		cursor = self.connection.cursor()
		query = "select data from `data` where dp != NULL"
		cursor.execute(query)
		threshold = 1
		cursor.scroll(0, 'absolute')
		while True:
			c = cursor.fetchone()
			if not c:
				break
			paras = json.loads(c[0].replace('\'','"'))


	def ipe(self):
		