import network
import blynklib_mp as bk
import random
from machine import Pin


# conect wifi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect("ssid", "password")


V2 = Pin(26, Pin.OUT)
V3 = Pin(27, Pin.OUT)
V4 = Pin(32, Pin.OUT)
V5 = Pin(33, Pin.OUT)



relay = [V2, V3, V4, V5]
relay_name = ['V2', 'V3', 'V4', 'V5']

print("conected")
#connect Blynk
BLYNK_AUTH = 'gTuoJT18C7OhBGBChvp-qzcs8dklvQXn'
blynk = bk.Blynk(BLYNK_AUTH)

print("authen OK")

    
def relay_onoff(relay_no, onoff):
    print("func Pin: {} value {}".format(relay_no, onoff))
    relay[relay_name.index(str(relay_no))].value(int(onoff))
    


@blynk.handle_event('read V*')  # Guage Temperature 
def read_virtual_pin_handler(pin):
    print("ESP -> Server V{}".format(pin))
    blynk.virtual_write(pin, random.randint(0, 100))
 

    
@blynk.handle_event('write V*') # button 1 
def write_virtual_pin_handler(pin, value):
    print("Server->ESP Write V{} Value{} ".format(pin, value))    
    relay_onoff("V{}".format(pin), "{}".format(value[0])) 
     
   

print("OK start"); 
while True:
    blynk.run()
