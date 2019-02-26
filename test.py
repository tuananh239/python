import Lib.vutuananh as math
a=5
b=7
c=[4,7,9,2,4,7,1]
i=[[2, 3],[1, 9],[6, 8]]
print('a =',a)
print('b =',b)

if math.check_prime(a) == 1:
	print(a,'la so nguyen to')
else:
	print(a,'khong phai la so nguyen to')
if math.check_prime(b) == 1:
	print(b,'la so nguyen to')
else:
	print(b,'khong phai la so nguyen to')

print(a,'+',b,'-',math.add(a,b))
print(a,'-',b,'=',math.sub(a,b))
print(a,'x',b,'=',math.mul(a,b))
print(a,'/',b,'=',math.div(a,b))

print('giai thua cua',a,'=',math.fact(a))
print('giai thua cua',b,'=',math.fact(b))
print(c)
print('day sap xep la:', math.sort_arr(c))
print(i)
print('ma tran sap xep la:', math.sort_matrix(i))
