#!/bin/sh

set -x
SQLITE_DB=${SQLITE_DB:-'data/temp.db'}

MON_HUM=/sys/bus/iio/devices/iio\:device0/in_humidityrelative_input
MON_TEMP=/sys/bus/iio/devices/iio\:device0/in_temp_input
MON_PRES=/sys/bus/iio/devices/iio\:device0/in_pressure_input

read_temp(){
  raw=$(cat $MON_HUM) && temp=$(echo "scale=3;$raw/1000" | bc) && 
    sqlite3 $SQLITE_DB "insert into adatok values('Paratartalom','$(date +'%Y-%m-%d %H:%M:%S')',$temp)" &&
    echo Paratartalom: $temp 

  raw=$(cat $MON_TEMP) && temp=$(echo "scale=3;$raw/1000" | bc) && 
    sqlite3 $SQLITE_DB "insert into adatok values('BME280','$(date +'%Y-%m-%d %H:%M:%S')',$temp)" &&
    echo BME280: $temp

  raw=$(cat $MON_PRES) && temp=$(echo "scale=3;$raw*10/1" | bc) && 
    sqlite3 $SQLITE_DB "insert into adatok values('Legnyomas','$(date +'%Y-%m-%d %H:%M:%S')',$temp)" &&
    echo Legnyomas: $temp
}

while :; do
  read_temp
  sleep 300
done

