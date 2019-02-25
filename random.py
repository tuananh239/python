import datetime
import time
import numpy

while(True):
	print("temp = {}, hum = {}, dust = {}".format(numpy.random.randint(0, 99), numpy.random.randint(0, 99), numpy.random.randint(0, 99)))
	time.sleep(2)

