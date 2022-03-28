import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
while True:
	if GPIO.input(36) == GPIO.HIGH:
		print("ok")
