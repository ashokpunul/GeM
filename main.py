import machine
import time
from machine import Pin, PWM
from umqtt.simple import MQTTClient
from time import sleep
import random
import json
import network
import sys
import gc
import micropython
from umqtt.simple import *
import ubinascii
#################MQTT###################

gc.collect()
#wifi_ssid = "Ashok_2.4G"
#wifi_password = "9663773243"

wifi_ssid = "iPhone"
wifi_password = "987654321a"

# Connect to WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(wifi_ssid, wifi_password)
while wlan.isconnected() == False:
  print('Waiting for connection...')
  time.sleep(1)
print("Connected to WiFi")


def connect_mqtt():
  global client_id, mqtt_server
  username="root"
  broker=  "165.22.213.30"
  topic = "test"
  #Mqtt_CLIENT_ID = "myyclientid123"
  Mqtt_CLIENT_ID = ubinascii.hexlify(machine.unique_id())
  PASSWORD="eadmin"  
  client = MQTTClient(client_id=Mqtt_CLIENT_ID, server=broker, port=1883, user=username, password=PASSWORD, keepalive=10000)
  client.connect()
  print('Connected to %s MQTT broker' % (client))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()


try:
  client = connect_mqtt()
except OSError as e:
  restart_and_reconnect()



last_message = 0
message_interval = 60

while True:
  try:
    if (time.time() - last_message) > message_interval:
      sensor_temp= machine.ADC(4)
      conversion_factor = 3.3 / (65535)
      rtc=machine.RTC()
      timestamp=rtc.datetime()
      reading = sensor_temp.read_u16()*conversion_factor
      temperature = 27 - (reading - 0.706)/0.001721
      location = "Kalkere-Blore"
      panel_id="PLN_001"
      device_id="D_001"
      temperature1= temperature
      timestring="%04d-%02d-%02d %02d:%02d:%02d"%(timestamp[0:3] + timestamp[4:7])
      location1=location
      topic = "test"
      #myjson3='This message from Raspberry Pi Pico'
      #myjson3 = {'panel_id': panel_id,'device_id': device_id,'temperature': temperature1,'insert_date': timestring,'location': location1}
      message = "\"'"+ str(panel_id)+"','"+ str(device_id)+"','"+str(temperature1)+"','"+str(timestring)+"','"+str(location1) +"'\""
      client.publish(topic,message)
      print(message)
      gc.collect()
      last_message = time.time()
  except OSError as e:
    restart_and_reconnect()

