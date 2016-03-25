import serial
import os
import shutil
import datetime
import time

ser = serial.Serial("/dev/ttyACM0",9600)
time.sleep(2) #arduinoのブート待ち
ser.write("z") #arduinoに文字列zを送信
f = open("sample.txt", 'w')
print("begin to measure")
oclock = datetime.datetime.today()
if 5 < oclock.hour < 19:
    for i in range (1,70):
        val = ser.readline()
        print(val)
        f.write(val)
f.close()
time = datetime.datetime.now()
newname = "{0:%Y%m%d-%H%M%S}.txt".format(time)
os.rename("sample.txt",newname)
ser.write("y") #arduinoに文字列yを送信
ser.close()
