#!/bin/bash
now=$(date +"%Y-%m-%dT%T.000Z")
echo $now
File="badtids"
Lines=$(cat $File)
for var in $Lines
do 
    echo $var
    docker exec -it mosquitto_server mosquitto_pub -h localhost -t "c72/HC72BE220800091/" -m "{\"hostname\":\"HC72BE220800091\",\"eventType\":\"tagInventory\",\"tagInventoryEvent\":{\"epc\":\"4oARkaUDAGGLW1SM\",\"epcHex\":\"E2801191A50300618B5B548C\",\"tid\":\"4oARkSAAdIxa2gMM\",\"tidHex\":\"$var\",\"antennaPort\":3,\"antennaName\":\"3\",\"peakRssiCdbm\":-6850,\"frequency\":916300,\"transmitPowerCdbm\":3300}}"    
    docker exec -it mosquitto_server mosquitto_pub -h localhost -t "c72/HC72BE220800091/" -m "{\"timestamp\":\"$now\",\"eventType\":\"tagInventory\",\"tagInventoryEvent\":{\"epc\":\"4oARkaUDAGGLW1SM\",\"epcHex\":\"E2801191A50300618B5B548C\",\"tid\":\"4oARkSAAdIxa2gMM\",\"tidHex\":\"$var\",\"antennaPort\":3,\"antennaName\":\"3\",\"peakRssiCdbm\":-6850,\"frequency\":916300,\"transmitPowerCdbm\":3300}}"    
    docker exec -it mosquitto_server mosquitto_pub -h localhost -t "c72/HC72BE220800091/" -m "{\"timestamp\":\"$now\",\"hostname\":\"HC72BE220800091\",\"tagInventoryEvent\":{\"epc\":\"4oARkaUDAGGLW1SM\",\"epcHex\":\"E2801191A50300618B5B548C\",\"tid\":\"4oARkSAAdIxa2gMM\",\"tidHex\":\"$var\",\"antennaPort\":3,\"antennaName\":\"3\",\"peakRssiCdbm\":-6850,\"frequency\":916300,\"transmitPowerCdbm\":3300}}"    
    docker exec -it mosquitto_server mosquitto_pub -h localhost -t "c72/HC72BE220800091/" -m "{\"timestamp\":\"$now\",\"hostname\":\"HC72BE220800091\",\"eventType\":\"tagInventory\"}"
    docker exec -it mosquitto_server mosquitto_pub -h localhost -t "c72/HC72BE220800091/" -m "{\"timestamp\":\"$now\",\"hostname\":\"HC72BE220800091\",\"eventType\":\"tagInventory\",\"tagInventoryEvent\":{\"epc\":\"4oARkaUDAGGLW1SM\",\"epcHex\":\"E2801191A50300618B5B548C\",\"tid\":\"4oARkSAAdIxa2gMM\",\"antennaPort\":3,\"antennaName\":\"3\",\"peakRssiCdbm\":-6850,\"frequency\":916300,\"transmitPowerCdbm\":3300}}"    
    docker exec -it mosquitto_server mosquitto_pub -h localhost -t "c72/HC72BE220800091/" -m "{\"timestamp\":\"$now\",\"hostname\":\"HC72BE220800091\",\"eventType\":\"tagInventory\",\"tagInventoryEvent\":{\"epc\":\"4oARkaUDAGGLW1SM\",\"epcHex\":\"E2801191A50300618B5B548C\",\"tid\":\"4oARkSAAdIxa2gMM\",\"tidHex\":\"$var\",\"antennaName\":\"3\",\"peakRssiCdbm\":-6850,\"frequency\":916300,\"transmitPowerCdbm\":3300}}"    
    docker exec -it mosquitto_server mosquitto_pub -h localhost -t "c72/HC72BE220800091/" -m "{\"timestamp\":\"$now\",\"hostname\":\"HC72BE220800091\",\"eventType\":\"tagInventory\",\"tagInventoryEvent\":{\"epc\":\"4oARkaUDAGGLW1SM\",\"epcHex\":\"E2801191A50300618B5B548C\",\"tid\":\"4oARkSAAdIxa2gMM\",\"tidHex\":\"$var\",\"antennaPort\":3,\"peakRssiCdbm\":-6850,\"frequency\":916300,\"transmitPowerCdbm\":3300}}"    
    docker exec -it mosquitto_server mosquitto_pub -h localhost -t "c72/HC72BE220800091/" -m "{\"timestamp\":\"$now\",\"hostname\":\"HC72BE220800091\",\"eventType\":\"tagInventory\",\"tagInventoryEvent\":{\"epc\":\"4oARkaUDAGGLW1SM\",\"epcHex\":\"E2801191A50300618B5B548C\",\"tid\":\"4oARkSAAdIxa2gMM\",\"tidHex\":\"$var\",\"antennaPort\":3,\"antennaName\":\"3\",\"frequency\":916300,\"transmitPowerCdbm\":3300}}"    
    docker exec -it mosquitto_server mosquitto_pub -h localhost -t "c72/HC72BE220800091/" -m "{\"timestamp\":\"$now\",\"hostname\":\"HC72BE220800091\",\"eventType\":\"tagInventory\",\"tagInventoryEvent\":{\"epc\":\"4oARkaUDAGGLW1SM\",\"epcHex\":\"E2801191A50300618B5B548C\",\"tid\":\"4oARkSAAdIxa2gMM\",\"tidHex\":\"$var\",\"antennaPort\":3,\"antennaName\":\"3\",\"peakRssiCdbm\":-6850,\"transmitPowerCdbm\":3300}}"    
    docker exec -it mosquitto_server mosquitto_pub -h localhost -t "c72/HC72BE220800091/" -m "{\"timestamp\":\"$now\",\"hostname\":\"HC72BE220800091\",\"eventType\":\"tagInventory\",\"tagInventoryEvent\":{\"epc\":\"4oARkaUDAGGLW1SM\",\"epcHex\":\"E2801191A50300618B5B548C\",\"tid\":\"4oARkSAAdIxa2gMM\",\"tidHex\":\"$var\",\"antennaPort\":3,\"antennaName\":\"3\",\"peakRssiCdbm\":-6850,\"frequency\":916300}}"
    
done