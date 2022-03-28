#!/usr/bin/env python

import sys
import time
import requests
import RPi.GPIO as GPIO
from mfrc522 import *

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

def changeLEDs(open):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(29, GPIO.OUT)
        GPIO.setup(31, GPIO.OUT)
        if (open == True):
                GPIO.output(29,GPIO.LOW)
                GPIO.output(31,GPIO.HIGH)
        else:
                GPIO.output(31,GPIO.LOW)
                GPIO.output(29,GPIO.HIGH)
if len(sys.argv) >1:
	ip = sys.argv[1]
else:
	ip = input("Enter Server IP:")
url = "http://"+ip+":8085/tool/server/receiver"
post = {"id":"test-pi"}
try:
	requests.get(url)
	print("Connected to Server")
except:
	print("Connection Failed")

reader = SimpleMFRC522()

while 1:
	changeLEDs(False)
	try:
		id, text = reader.read()
		post["value"]= id
		web = requests.post(url, data=post)
		print("Data Found")
		responce = web.text
		if "Request Confirmed" in responce:
			print("yes")
			changeLEDs(True)
			time.sleep(2)
		else:
			print("no")
			GPIO.setmode(GPIO.BOARD)
			GPIO.setup(29, GPIO.OUT)
			GPIO.output(29, GPIO.LOW)



		time.sleep(2)
	finally:
		GPIO.cleanup()
