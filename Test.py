# !/usr/bin/env python

"""
            ／￣￣￣￣￣￣￣￣
　　　　　　  |　Info about the project comes here..
　　　　　　  ＼＿＿　＿＿＿＿＿＿＿
　　　　　　　　　  ∨
            ██████████  ████
        ████▒▒░░░░░░░░██▒▒░░██
      ██▒▒░░░░██░░██░░░░██░░░░██
    ██▒▒░░░░░░██░░██░░░░░░▒▒░░██
    ██░░░░░░░░██░░██░░░░░░▒▒▒▒██
  ██░░░░░░▒▒▒▒░░░░░░▒▒▒▒░░░░▒▒██
██▒▒░░░░░░░░░░░░██░░░░░░░░░░░░██
██░░░░▒▒░░░░░░░░██░░░░░░░░░░▒▒██
██░░░░▒▒░░░░░░░░░░░░░░░░░░░░██  
  ██████░░░░░░░░░░░░░░░░░░▒▒██  
██▒▒▒▒▒▒██░░░░░░░░░░░░░░░░▒▒██  
██▒▒▒▒▒▒▒▒██░░░░░░░░░░░░▒▒██    
██▒▒▒▒▒▒▒▒██░░░░░░░░░░▒▒████    
  ██▒▒▒▒▒▒▒▒██▒▒▒▒▒▒████▒▒▒▒██  
    ██▒▒▒▒██████████▒▒▒▒▒▒▒▒▒▒██
      ██████      ████████████  
"""

# IMPORTS
from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

# CONFIG
IP = PiGPIOFactory(host='192.168.0.123')
lamp = LED(17, pin_factory=IP)

# AUTHOR INFORMATION
__author__ = "Tibo Smet"
__email__ = "tibo.smet@student.kdg.be"
__status__ = "Development"


def main():
    lamp.toggle()
    sleep(1)
    lamp.toggle()
    sleep(1)


if __name__ == '__main__':
    main()
