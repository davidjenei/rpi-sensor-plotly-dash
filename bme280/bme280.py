import sqlite3 as lite

con = lite.connect('/data/temp.db')
ido = time.strftime("%Y-%m-%d %H:%M:%S")

# /sys/bus/iio/devices/iio\:device0/in_pressure_input
# Returns pressure in Pa as unsigned 32 bit integer in Q24.8 format (24
# * integer bits and 8 fractional bits).  Output value of "24674867"
# * represents 24674867/256 = 96386.2 Pa = 963.862 hPa

# /sys/bus/iio/devices/iio\:device0/in_humidityrelative_input
# Returns humidity in percent, resolution is 0.01 percent. Output value of
# * "47445" represents 47445/1024 = 46.333 %RH.

# /sys/bus/iio/devices/iio\:device0/in_temp_input
# resolution is 0.01 DegC

legnyomas = '{0:0.1f}' .format(hectopascals)
homerseklet = '{0:0.1f}' .format(degrees)
paratartalom = '{0:0.1f}' .format(humidity)

with con:
  cur = con.cursor()
  cur.execute("INSERT INTO adatok VALUES(?,?,?)",('Legnyomas',ido,legnyomas))
  cur.execute("INSERT INTO adatok VALUES(?,?,?)",('Paratartalom', ido, paratartalom))
  cur.execute("INSERT INTO adatok VALUES(?,?,?)",('BME280',ido,homerseklet))

