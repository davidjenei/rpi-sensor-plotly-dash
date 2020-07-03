import os
import sqlite3
import time
from select import poll, POLLPRI

db = os.environ.get('SQLITE_DB', 'temp.db')
conn = sqlite3.connect(db)
cur = conn.cursor()

try:
    with open('/sys/class/gpio/export', 'w') as f:
        f.write('7')

    with open('/sys/class/gpio/gpio7/direction', 'w') as f:
        f.write('in')

    with open('/sys/class/gpio/gpio7/edge', 'w') as f:
        f.write('both')
except:
    pass

fd = os.open('/sys/class/gpio/gpio7/value',os.O_RDONLY)
p = poll()
p.register(fd, POLLPRI)

while True:
    events = p.poll()
    for e in events:
        ts = time.strftime("%Y-%m-%d %H:%M:%S")
        val = int(os.read(fd, 1))
        print('{} {}'.format(ts,val))
        cur.execute("INSERT INTO adatok VALUES(?,?,?)",("PIR",ts,val))
        conn.commit()
    os.lseek(fd,0,0)
