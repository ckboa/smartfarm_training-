import network
import blynklib_mp as bk
import random
from machine import Pin, SoftI2C, ADC
import dht
import ssd1306




# conect wifi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect("ssid", "password")


#  init  sensor and display
sensor = dht.DHT22(Pin(5))
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
display = ssd1306.SSD1306_I2C(128, 64, i2c)
adc35 = ADC(Pin(39))  


#init relay 
V2 = Pin(26, Pin.OUT)
V3 = Pin(27, Pin.OUT)
V4 = Pin(32, Pin.OUT)
V5 = Pin(33, Pin.OUT)



relay = [V2, V3, V4, V5]
relay_name = ['V2', 'V3', 'V4', 'V5']
relay_state = [0, 0, 0, 0]

print("conected")
#connect Blynk
BLYNK_AUTH = '...... token ...............'
blynk = bk.Blynk(BLYNK_AUTH)

print("authen OK")


def relay_display():
    relay_text1 = "relay 1:{} 2:{}".format(relay_state[0],relay_state[1])
    relay_text2 = "      3:{} 4:{}".format(relay_state[2], relay_state[3])
    display.text(relay_text1, 0, 40)
    display.text(relay_text2, 0, 50)    
    display.show()     

def reading_sensor():
    print("sensor reading")
    display.fill(0)
    sensor.measure()
    temp = sensor.temperature()
    humi = sensor.humidity()
    soil = adc35.read() 
    display.text("Temp %3.1f" %temp, 0, 0)
    display.text("Humi %3.1f" %humi, 0, 10)
    display.text("Soil %d" %soil, 0, 20)
    blynk.virtual_write(0, temp)
    blynk.virtual_write(1, humi)
    blynk.virtual_write(6, soil)
    relay_display()
    display.show()
  
    
def relay_onoff(relay_no, onoff):
    print("func Pin: {} value {}".format(relay_no, onoff))
    relay[relay_name.index(str(relay_no))].value(int(onoff))
    relay_state[relay_name.index(str(relay_no))] = int(onoff)     
    relay_display()
    display.show()    
    


@blynk.handle_event('read V*')  # Guage Temperature 
def read_virtual_pin_handler(pin):
    print("ESP -> Server READ V{}".format(pin))
    reading_sensor();

    
@blynk.handle_event('write V*') # button 1 
def write_virtual_pin_handler(pin, value):
    print("Server->ESP Write V{} Value{} ".format(pin, value))    
    relay_onoff("V{}".format(pin), "{}".format(value[0])) 

   

print("OK start"); 
while True:
    blynk.run()



