from pyModbusTCP.client import ModbusClient
from datetime import datetime
from struct import *
from electrical import setup_read

an_id=1
setup_read(an_id)
print(" ")
an_id=2
setup_read(an_id)
print(" ")
