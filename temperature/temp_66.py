#!/usr/bin/python3

import mcp9600
import time

m = mcp9600.MCP9600(i2c_addr=0x66)

m.set_thermocouple_type('K')

t = m.get_hot_junction_temperature()
# c = m.get_cold_junction_temperature()
# d = m.get_temperature_delta()

# print(t, c, d)
print(t)

exit()
