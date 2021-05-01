from machine import  Pin 
import utime

relay1 = Pin(26, Pin.OUT)
relay2 = Pin(27, Pin.OUT)
relay3 = Pin(32, Pin.OUT)
relay4 = Pin(33, Pin.OUT)

relay_list = [relay1, relay2, relay3, relay4]

def on_relay(relay):
    relay.value(0)

def off_relay(relay):
    relay.value(1)

for i in relay_list:
    on_relay(i)
    utime.sleep(2)
    off_relay(i)
    

