from gpiozero import AngularServo
from time import sleep
from gpiozero.pins.lgpio import LGPIOFactory
factory = LGPIOFactory()

servo = AngularServo(18, 
                     min_pulse_width=0.0006, 
                     max_pulse_width=0.0023, 
                     pin_factory=factory)

try:
    print("Servo is moving... Press Ctrl+C to stop.")
    while True:
        servo.angle = 67
        sleep(5)
        servo.angle = 0
        sleep(1)
        servo.angle = -67
        sleep(1)
finally:
    servo.angle = 0
    sleep(0.5)
    servo.detach()