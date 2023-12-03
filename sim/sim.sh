#!/bin/bash
now=$(date +"%Y-%m-%dT%T.000Z")
echo $now
File="simtids"
Lines=$(cat $File)
for var in $Lines
do 
    echo $var
    docker exec -it mosquitto_server mosquitto_pub -h localhost -t "c72/HC72BE220800091/" -m "{\"timestamp\":\"$now\",\"hostname\":\"HC72BE220800091\",\"eventType\":\"tagInventory\",\"tagInventoryEvent\":{\"epc\":\"4oARkaUDAGGLW1SM\",\"epcHex\":\"E2801191A50300618B5B548C\",\"tid\":\"4oARkSAAdIxa2gMM\",\"tidHex\":\"$var\",\"antennaPort\":3,\"antennaName\":\"3\",\"peakRssiCdbm\":-6850,\"frequency\":916300,\"transmitPowerCdbm\":3300}}"    
done