#!/usr/bin/python -u
import signal
from mqtt import mqttc,connectMqtt

# on Ctrl-C handler
def handler(signum, frame):    
    print('Stopping mqtt monitoring client..')
    mqttc.loop_stop()
    print("Stopped mqtt monitoring client.")
    exit(1)

signal.signal(signal.SIGINT, handler)

connectMqtt()
    
mqttc.loop_forever()
