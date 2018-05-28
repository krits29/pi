import RPi.GPIO as GPIO

buzzeRPin = 11
buttonPin = 12

def setup():
    GPIO.setmode(GPIO.BOARD) # Numbers GPIOs by physical location
    GPIO.setup(buzzeRPin, GPIO.OUT) # Set buzzeRPin's mode is output
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def loop():
    while True:
        if GPIO.input(buttonPin)==GPIO.LOW:
            GPIO.output(buzzeRPin,GPIO.HIGH)
        else:
            GPIO.output(buzzeRPin,GPIO.LOW)

def destroy():
    GPIO.output(buzzeRPin, GPIO.LOW)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
            
