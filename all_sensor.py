from machine import Pin, SoftI2C, ADC
import ssd1306
import dht
import utime


# display setting 
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

# Temperature/Huminity Sensor setting
sensor = dht.DHT22(Pin(16))

# soil setting  
adc35 = ADC(Pin(35))   
adc35.atten(ADC.ATTN_11DB)    
adc35.width(ADC.WIDTH_12BIT)  

# reading 
def reading_sensor():
    sensor.measure()
    temp_str = "Temp: {0:3.1f}".format(sensor.temperature())
    humi_str = "Humi: {0:3.1f}".format(sensor.humidity())
    soil_str = "soil: {}".format(adc35.read()) 
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