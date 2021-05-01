import network
import blynklib_mp as bk
import random

# conect wifi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect("ssid", "password")

print("conected")
#connect Blynk
BLYNK_AUTH = 'gTuoJT18C7OhBGBChvp-qzcs8dklvQXn'
blynk = bk.Blynk(BLYNK_AUTH)


@blynk.handle_event('read V0')  # Guage Temperature 
def read_virtual_pin_handler(pin):
    print("ESP->Server")
    blynk.virtual_write(pin, random.randint(0, 100))
    
@blynk.handle_event('write V2') # button 1 
def write_virtual_pin_handler(pin, value):
    print("Server->ESP".format(pin, value))    

print("OK start"); 
while True:
    blynk.run()