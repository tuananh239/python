def add(a,b):
	return a+b

def mul(a,b):
	return a*b

def sub(a,b):
	return a-b

def div(a,b):
	return a/b

def fact(a):
	t = 1
	if a == 0 or a == 1:
		return 1
	else:
		for i in range(2,a+1):
			t = t*i
		return t

def check_prime(a):
	for i in range(2,a):
		if a % i == 0:
			return 0;		
	return 1

def sort_arr(a):
	for i in range(0,len(a)-1):
		for j in range(i,len(a)):
			if a[i] > a[j]:
				#swap(a[i],a[j])
				#temp = a[i]
				#a[i] = a[j]
				#a[j] = temp
				[a[i], a[j]] = [a[j], a[i]]
	return a

def sort_matrix(a):
	n = 0
	b = {}
	for i in range(len(a)):
		for j in range(len(a[i])):
			b[n] = a[i][j]
			n += 1
	sort_arr(b)
	n = 0
	for i in range(len(a)):
		for j in range(len(a[i])):
			a[i][j] = b[n]
			n += 1
	return a
