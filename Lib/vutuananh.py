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
	return 1;

def sort_arr(a):
	for i in range(0,len(a)-1):
		for j in range(i,len(a)):
			if a[i] > a[j]:
				#swap(a[i],a[j])
				temp = a[i]
				a[i] = a[j]
				a[j] = temp
	return a

def sort_matrix(a):
	n = 0
	for i in range(0,len(a)-1):
		for j in range(0,len(a[i])-1):
			b[n] = a[i][j]
			n += 1
	sort_arr(b)
	n = 0
	for i in range(0,len(a)-1):
		for j in range(0,len(a[i])-1):
			a[i][j] = b[n]
			n += 1
	return b
I = ([[5, 6], [4, 3], [1, 2]])
print(I)
print(sort_matrix(I))
