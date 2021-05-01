import network
import blynklib_mp as bk
import random
from machine import Pin

# conect wifi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect("ssid", "password")
#add relay ..
relay1 = Pin(26, Pin.OUT)

print("conected")
#connect Blynk
BLYNK_AUTH = 'gTuoJT18C7OhBGBChvp-qzcs8dklvQXn'
blynk = bk.Blynk(BLYNK_AUTH)

print("authenOK")
@blynk.handle_event('read V0')  # Guage Temperature 
def read_virtual_pin_handler(pin):
    print("ESP->Server")
    blynk.virtual_write(pin, random.randint(0, 255))
    
@blynk.handle_event('write V2') # button 1 
def write_virtual_pin_handler(pin, value):
    print("Server->ESP".format(pin, value))  
    # check the value here 
    if(int(value[0]) == 0):
      print("on  {0}".format(value[0]))   
      relay1.value(0)
    else:
      print("off  {0}".format(value[0])) 
      relay1.value(1)

print("OK start"); 
while True:
    blynk.run()

