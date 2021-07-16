from machine import Pin, SoftI2C, ADC
import ssd1306
import dht
import utime




# display setting 
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

# Temperature/Huminity Sensor setting
sensor = dht.DHT22(Pin(15))  # 15 for board  # 16 for breadboard

# soil setting  
adc35 = ADC(Pin(35))   
adc35.atten(ADC.ATTN_11DB)    
adc35.width(ADC.WIDTH_12BIT)  

#assign relay 
relay1 = Pin(26, Pin.OUT)
relay2 = Pin(27, Pin.OUT)
relay3 = Pin(32, Pin.OUT)
relay4 = Pin(33, Pin.OUT)


def on_relay(relay):
    relay.value(0)

def off_relay(relay):
    relay.value(1)


def soil_moisture(soil_value):
    if(soil_value > 1000):
        on_relay(relay1)
    else:
        off_relay(relay1)    




# reading 
def reading_sensor():
    sensor.measure()
    temp_str = "Temp: {0:3.1f}".format(sensor.temperature())
    humi_str = "Humi: {0:3.1f}".format(sensor.humidity())
    soil_str = "soil: {}".format(adc35.read()) 
    soil_moisture(adc35.read())
    # set text display
    display.fill(0)
    display.show()      
    display.text(temp_str, 0, 0)
    display.text(humi_str, 0, 10)
    display.text(soil_str, 0, 20)
    display.show() 

while(1):
    reading_sensor()
    utime.sleep(5)