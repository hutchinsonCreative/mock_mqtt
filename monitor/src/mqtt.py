import paho.mqtt.client as mqtt
import json
import os
import time
from threading import Thread, Lock
from colours import teal,white,orange,red, green,blue, grey
from datetime import datetime,timedelta
from dotenv import find_dotenv, load_dotenv
from MessageValidator import MessageValidator

print(f"\n\n{blue()}MQTT Monitoring Client & Message Validator\n")

load_dotenv(find_dotenv())

validator = MessageValidator()

# MQTT Settings
print(f"{white()}Loading MQTT Settings from .env ...")
MQTT_Broker = os.getenv('MQTT_HOST')
MQTT_Port = int(os.getenv('MQTT_PORT'))
Keep_Alive_Interval = int(os.getenv('MQTT_ALIVE_INTERVAL'))
MQTT_Topic = str(os.getenv('MQTT_TOPIC'))
print(f"{white()}Host:       {orange()}{MQTT_Broker}")
print(f"{white()}Port:       {orange()}{MQTT_Port}")
print(f"{white()}Keep Alive: {orange()}{Keep_Alive_Interval}")
print(f"{white()}Topic:      {orange()}{MQTT_Topic}\n")

# Subscription status flag
mqtt_subscribed = False


# Subscribe
def on_connect(client, userdata, flags, rc, properties=None):
  print(f"{teal()}MQTT Connected!")
  mqtt_subscribed = True
  mqttc.subscribe(MQTT_Topic, 2)

def on_disconnect(client, userdata, rc):
  print(f"{orange()}MQTT Disconnected!")
  mqtt_subscribed = False
  print(f"{grey()}Reason: {rc}")

def on_subscribe(mosq, obj, mid, granted_qos,properties=None):
  print(f"{teal()}Granted QOS: {granted_qos}")
  pass

def on_message(mosq, obj, msg):
  try:  
    json_object = json.loads(msg.payload.decode('utf-8'))    
    valid = validator.validate(msg,json_object)    
      
  except Exception as e:
    jo = json.loads(msg.payload.decode('utf-8'))
    print(f"{orange()}Error {str(e)}\n{jo}")

# Initialise client      
mqttc = mqtt.Client("MonitoringClient",False,protocol=3)

# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe
mqttc.on_disconnect = on_disconnect

# Connect
def connectMqtt():
  connected = False
  attempt = 0
  while connected == False:
    print(f"{teal()}Connecting to MQTT host: {blue()}{MQTT_Broker}{teal()}:{blue()}{MQTT_Port}")
    attempt +=1
    try:
      mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))
      # mqttc.tls_set(ca_certs="ca.crt", tls_version=ssl.PROTOCOL_TLSv1_2)
      connected = True
    except Exception as e:
      if attempt == 1: print(f"{orange()}Error connecting to MQTT.{blue()}{MQTT_Broker} {MQTT_Port} {orange()}Attempt {blue()}{attempt} {grey()}\n{str(e)} ")
      time.sleep(0.5)
      print(".",end="")
