import glob
import time
import os
import datetime
import sqlite3 as lite
import sys

# 0315046115ff - szoba
# 0215033db1ff - konyha
# 0315044fb8ff - Anett szoba
# 0215032475ff - Nappali
# 031504611eff - Erkely

while True:
    with con:
        cur = con.cursor()
        cur.execute("INSERT INTO adatok VALUES(?,?,?)",(hely[1],ido,temp_C))

     time.sleep(300)

