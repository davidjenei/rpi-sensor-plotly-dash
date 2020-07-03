#!/bin/sh

SQLITE_DB=${SQLITE_DB:-'data/temp.db'}
MON_ANETT=/sys/class/hwmon/hwmon1/temp1_input
MON_ERKELY=/sys/class/hwmon/hwmon2/temp1_input
MON_NAPPALI=/sys/class/hwmon/hwmon3/temp1_input

read_temp(){
  raw=$(cat $MON_ANETT) && temp=$(echo "scale=3;$raw/1000" | bc) && 
    sqlite3 $SQLITE_DB "insert into adatok values('Anett szoba','$(date +'%Y-%m-%d %H:%M:%S')',$temp)" &&
    echo Anett szoba: $temp

  raw=$(cat $MON_ERKELY) && temp=$(echo "scale=3;$raw/1000" | bc) && 
    sqlite3 $SQLITE_DB "insert into adatok values('Erkely','$(date +'%Y-%m-%d %H:%M:%S')',$temp)" &&
    echo Erkely: $temp

  raw=$(cat $MON_NAPPALI) && temp=$(echo "scale=3;$raw/1000" | bc) && 
    sqlite3 $SQLITE_DB "insert into adatok values('Nappali','$(date +'%Y-%m-%d %H:%M:%S')',$temp)" &&
    echo Nappali: $temp
}

while :; do
  read_temp
  sleep 300
done

