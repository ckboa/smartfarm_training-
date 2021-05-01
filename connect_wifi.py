import network
 
def connect():
  ssid = "ssid"
  password =  "password"
 
  station = network.WLAN(network.STA_IF)
 
  if station.isconnected() == True:
      print("Already connected")
      return
 
  station.active(True)
  station.connect(ssid, password)
 
  while station.isconnected() == False:
      pass
 
  print("Connection successfully")
  print(station.ifconfig())

connect()