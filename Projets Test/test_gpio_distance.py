from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

factory = PiGPIOFactory(host='192.168.1.186')
led11 = LED(11, pin_factory=factory)
led17 = LED(17, pin_factory=factory)

while True:
    led11.on()
    sleep(1)
    led11.off()
    sleep(1)

    led17.on()
    sleep(1)
    #led17.off()
    sleep(1)