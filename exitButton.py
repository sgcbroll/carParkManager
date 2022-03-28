import sys
import requests
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
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

if len(sys.argv) >3:
	ip = sys.argv[3]
else:
	ip = input("Enter Server IP:")
url = "http://"+ip+":8085/tool/server/receiver"
if ((sys.argv[2].lower()) == "entry"):
	change = 1
else:
	change = -1
post = {"id":sys.argv[1],"change":change}
try:
	requests.get(url)
	print("Button connected to Server on "+ip)
except:
	print("Button connection Failed")

while True:
	if GPIO.input(36) == GPIO.HIGH:
		post["value"]= "0"
		web = requests.post(url, data=post)
		print("Button Pressed")
		responce = web.text
		if "Request Confirmed" in responce:
			changeLEDs(True)
			time.sleep(2)
