from machine import Pin
import dht
sensor = dht.DHT22(Pin(16))
sensor.measure()
temp = sensor.temperature()
humi = sensor.humidity()
print("temperature: %3.1f" %temp)
print("Huminity: %3.1f" %humi)