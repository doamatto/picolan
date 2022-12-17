import network
import time
from machine import Pin, Timer

# enable station interface
nic = network.WLAN(network.AP_IF)
nic.config(
	ssid='PicoLAN',
	#channel=11,
	#hidden=False,
	#security=CYW43_AUTH_WPA2_AES_PSK,
	key='ronchetto')
nic.ifconfig(('10.0.10.1','255.255.0.0', '10.0.10.1', '1.1.1.1'))
nic.active(True)

# blink LED
tim = Timer()
led = machine.Pin('LED', machine.Pin.OUT)
def tick(timer):
	global led
	led.toggle()
tim.init(freq=2.5, mode=Timer.PERIODIC, callback=tick)

# nic.config(pm) # Debugging

#while True:
	#if nic.isconnected():
		# if it's being used, we don't need to be so "eco-friendly"
		#nic.config(pm= 0xa11140)
	#else:
		#nic.config(pm= ???) # need to use Pico to get initial pm value
