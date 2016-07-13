while True:
	import os
	import datetime
	import time
	import serial
	import os
	import shutil

	os.mkdir("sample")

	oclock = datetime.datetime.today()

	while 6 <= oclock.hour <= 20:
		import serial
		import os
		import shutil
		import time

		os.chdir("/home/ienaga/デスクトップ/solar_measure/python_programing/sample") #change directly
		ser = serial.Serial("/dev/ttyACM0",9600)
		time.sleep(2)
		ser.write(b'z')
		serial = open("sample.txt", 'w')
		print("begin to measure")

		for i in range (1,50):
			val = ser.readline()
			print(val.decode('utf-8'))
			serial.write(val.decode('utf-8'))

		serial.close()

		ser.write(b"y")

		#text file caluculate
		from matplotlib import pyplot as plt
		import numpy as np

		fig = plt.figure()
		data = np.loadtxt('sample.txt',delimiter = ',',unpack = True)

		plot1 = data[:,0]
		plot2 = data[:,1]

		x = (plot1*55)/1023
		y = (plot2*5)/(1023*11)

		plt.plot(x,y)
		plt.savefig('sample.png')
		#text file calculate finish

		dailytime = datetime.datetime.now()
		newname = "{0:%Y-%m-%d-%H-%M:%S}.png".format(dailytime)
		os.rename("sample.png",newname)
		
		import os
		os.remove('sample.txt')

		#os.chdir("/home/ienaga/デスクトップ/uploader/public/graph") #change directly
		#plt.savefig('sample.png')
		
		time.sleep(10.0)

		ser.close()

	while oclock.hour > 20:
		os.chdir("/home/pi/Desktop/python_programing") #change directly
		newdate = datetime.datetime.now()
		newname = "{0:%Y-%m-%d}".format(newdate)
		os.rename("sample",newname)
		
		time.sleep(60)

	while oclock.hour < 5:
		time.sleep(120)


def png():   #sub function 
	import os
	from matplotlib import pyplot as plt
	import numpy as np

	x,y = np.loadtxt('sample.txt',delimiter = ',',unpack = True)
	plt.plot(x,y)
	plt.savefig('sample.png')

	dailytime = datetime.datetime.now()
	newname = "{0:%Y-%m-%d-%H-%M:%S}.png".format(dailytime)
	os.rename("sample.png",newname)