from datetime import datetime, timedelta
from colours import red, green,white,blue,teal,brown,grey,orange,purple,pink

class MessageValidator():
    def __init__(self):        
        self.something = 1
        
    def validate(self,msg,json_object):
        valid = True
        if not 'eventType' in json_object:
            print(f"{red()}Missing eventType")
            valid = False
                    
        eventType= json_object['eventType']
        
        if eventType != "tagInventory":
            print(f"{red()}eventType should be of type tagInventory")
            valid = False
        
        if not 'timestamp' in json_object:
            print(f"{red()}Missing timestamp")
            valid = False
            timestamp = "1970-01-01T16:20:22.000Z"
        
        tl = len(json_object['timestamp'])
        timestamp = json_object['timestamp']
        timestamp = timestamp[0:tl-1]
        
        if not 'hostname' in json_object:
            print(f"{red()}Missing `hostname`")
            valid = False
            hostname = "Missing hostname"
        else:
            hostname = json_object['hostname']
        
        if not 'tagInventoryEvent' in json_object:
            print(f"{red()}Missing tagInventoryEvent object")
            valid = False
        if eventType == "tagInventory":            
            topic = msg.topic
        
        try:
            tidHex = json_object['tagInventoryEvent']['tidHex']
        except Exception as e:
            tidHex = ""
            valid = False
            print(f"{red()}Missing tidHex")
            
        try:
            antennaPort = json_object['tagInventoryEvent']['antennaPort']
        except Exception as e:
            print(f"{red()}Missing antennaPort")
            valid = False
            antennaPort = 0
        try:
            antennaName = json_object['tagInventoryEvent']['antennaName']
        except Exception as e:
            print(f"{red()}Missing antennaName")
            valid = False
            antennaName = ""
        try:
            peakRssiCdbm = json_object['tagInventoryEvent']['peakRssiCdbm']
        except Exception as e:
            print(f"{red()}Missing peakRssiCdbm")
            valid = False
            peakRssiCdbm = 0
        try:
            frequency = json_object['tagInventoryEvent']['frequency']
        except Exception as e:
            print(f"{red()}Missing frequency")
            valid = False
            frequency = 0
        try:
            transmitPowerCdbm = json_object['tagInventoryEvent']['transmitPowerCdbm']
        except Exception as e:
            print(f"{red()}Missing transmitPowerCdbm")
            valid = False
            transmitPowerCdbm = 0
        c = green() if valid else orange()
        print(f"{white()}Valid {c}{valid} {white()}Topic: {orange()}[{topic}] {white()}Timestamp: {orange()}[{timestamp}] {white()} hostname {teal()}[{hostname}] {white()}tidHex {teal()}[{tidHex}] {white()}antennaPort {teal()}[{antennaPort}] {white()}antennaName {teal()}[{antennaName}] {white()} peakRssiCdbm {teal()}[{peakRssiCdbm}] {white()}frequency {teal()}[{frequency}] {white()}transmitPowerCdbm {teal()}[{transmitPowerCdbm}]")
        if not valid: print(f"")
        return True