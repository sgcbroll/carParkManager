import sys
import cv2
import time
import requests
import RPi.GPIO as GPIO

def changeLEDs(open):
	if (open == True):
		GPIO.output(5,GPIO.LOW)
		GPIO.output(6,GPIO.HIGH)
	else:
		GPIO.output(6,GPIO.LOW)
		GPIO.output(5,GPIO.HIGH)
if len(sys.argv) > 3:
	ip = sys.argv[3]
else:
	ip = input("Enter Server IP: ")
url = "http://"+ip+":8085/tool/server/receiver"
post = {"id":sys.argv[1],"change":sys.argv[2]}
try:
	requests.get(url)
	print("QR Sensor connected to Server on "+ip)
except:
	print("QR Sensor connection to Server has failed")


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.output(5, GPIO.HIGH)
GPIO.output(6, GPIO.LOW)

cap = cv2.VideoCapture(0)
dectector = cv2.QRCodeDetector()

while True:
	try:
		_, img = cap.read()
		data, bbox, _ = dectector.detectAndDecode(img)
		if (bbox is not None):
			cv2.putText(img, data, (int(bbox[0][0][0]), int(bbox[0][0][1])-20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0),2)
			if data and data != lastdata:
				print("data found: ", data)
				post["value"] = data
				lastdata = data;
				web = requests.post(url, data=post)
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
				changeLEDs(False)
		cv2.imshow("code detector", img)
		cv2.waitKey(1)		
	except KeyboardInterrupt:
		cap.release()
		cv2.destroyAllWindows()
		break
	#except:
		#print("error while reading: continuing to read")
#cv2.destroyAllWindows()
