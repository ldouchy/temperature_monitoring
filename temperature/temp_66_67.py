#!/usr/bin/python3

import mcp9600
import time
from datetime import datetime
import psycopg2

now = datetime.utcnow()
date_str = now.strftime("%Y-%m-%d %H:%M:%S")

m66 = mcp9600.MCP9600(i2c_addr=0x66)
m66.set_thermocouple_type('K')

t66 = m66.get_hot_junction_temperature()

time.sleep(5.0)

m67 = mcp9600.MCP9600(i2c_addr=0x67)
m67.set_thermocouple_type('K')

t67 = m67.get_hot_junction_temperature()


print(f'{date_str};{t66};{t67}')

conn = psycopg2.connect(
    host="192.168.1.116",
    database="homesweethome",
    user="postgres",
    password="mysecretpassword")

cur = conn.cursor()

cur.execute("INSERT INTO box_experiment_01 (date, probe_t1, probe_t2) VALUES(%s,%s,%s)", (date_str,t66,t67))
conn.commit()
cur.close()
conn.close()
