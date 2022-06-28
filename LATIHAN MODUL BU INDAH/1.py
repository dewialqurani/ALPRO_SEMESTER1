def sig (x):
	n = len(x)
	w = 0
	temp = 0
	for a in range(n) :
		if x[a]>=10 :
			w = 1
		else :
			w = 0
		temp = temp + (x[a]*w)
	total = (1/n) * temp
	return total
	
data = [5,10,25]
print(sig(data))