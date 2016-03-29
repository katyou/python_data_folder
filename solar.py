while True:

	import serial
	import os
	import shutil
	import datetime
	import time

	oclock = datetime.datetime.today()
	if 5 < oclock.hour < 19:
		ser = serial.Serial("/dev/ttyACM0",9600)
		time.sleep(2)
		ser.write(b'z')
		serial = open("sample.txt", 'w')
		print("begin to measure")

		for i in range (1,70):
			val = ser.readline()
			print(val.decode('utf-8'))
			serial.write(val.decode('utf-8'))

		serial.close()

		from matplotlib import pyplot as plt
		import numpy as np
		x,y = np.loadtxt('sample.txt',delimiter=',',unpack=True)
		plt.plot(x,y)
		plt.savefig('sample.png')

		time = datetime.datetime.now()
		newname = "{0:%Y%m%d-%H%M%S}.png".format(time)
		os.rename("sample.png",newname)

		ser.write(b"y")
		import time
		time.sleep(30.0)
		ser.close()