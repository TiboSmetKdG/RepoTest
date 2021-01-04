#!/usr/bin/env python
"""
Tijdens je project voor Simulate is samenwerking in team van cruciaal belang. Niet alleen op communicatief vlak of planning. Maar ook bij de ontwikkeling van software. Later zal je op je werkplek ook vaak moeten samenwerken via een Version Control Systrem (VCS) zoals GitHub.
Sommige inzichten in hoe dit allemaal werkt zijn niet altijd even simpel. Leren werken met een VCS is een proces waarin we door veelvuldig doen gaan groeien.

Met deze opdracht gaan we concreter starten aan het tegemoetkomen van dit doel.
"""

from gpiozero import LED
import time
from gpiozero.pins.pigpio import PiGPIOFactory

...

_author_ = "Senne De Winter"
_email_ = "senne.dewinter@student.kdg.be"
_status_ = "Development"

IP = PiGPIOFactory(host='192.18.1.39')
LED = LED(6, pin_factory=IP)


def main():
    LED.on()
    time.sleep(5)
    LED.off()
    time.sleep(5)


if __name__ == '_main_':  # code to execute if called from command-line
    main()
