from random import randint
from time import sleep
from datetime import datetime

print('chuong trinh lay gia tri ngau nhien')

try:
	while(1):
		temp = randint(28,30)
		hum = randint(60,80)
		time_now = datetime.now()
		print ('Cap nhat luc %s' %time_now)
		print ('Nhiet do: %s' %temp)
		print ('Do am: %s' %hum)
		sleep(1)

except KeyboardInterrupt:
	print('Chuong trinh ket thuc')
