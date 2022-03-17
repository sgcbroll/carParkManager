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

reader = SimpleMFRC522()

while 1:
	changeLEDs(False)
	try:
		id, text = reader.read()
		post["value"]= id
		requests.post(url, data=post)
		print("Data Found")
		changeLEDs(True)
		time.sleep(4)
	finally:
		GPIO.cleanup()
