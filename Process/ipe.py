def getTextSet(p):
#input pi = {(t1,f1),(t2,f2)...(tn,fn)}
	l=[]
	for i in p : 
		l.append(i[0])
	return l
#output ti = { t1, t2 ,t3 ..tn }

# Format 
#NDP = [['','']['','']['','']['','']['',''].....['', '']]

def suffling(nd , Dnd , NDP,u ):
	for p in Dnd :
		termset = getTextset(p)
		flag = 1
		for t in termset : 
			if t in nd :
				flag = 0 
			else :
				flag = 1 

		if flag is 0 : # all terms are in nd | remove complete conflict 
			new_NDP  = []
			for p in NDP : 
				for t in termset :	
					if p[0] is t : 
						
				
				
	
