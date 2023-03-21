from pyModbusTCP.client import ModbusClient
from struct import *
from datetime import datetime
import time

# TCP auto connect on first modbus request
c = ModbusClient(host="192.168.1.254", port=502, unit_id=1, auto_open=True)

################################################
#PF   Average    PF                   3007 Float
#VLL  Average    line to line voltage 3009 Float
#VLN  Average    line to neutral      3011 Float
#A    Average    current              3013 Float
#F    Frequency, Hz                   3015 Float
#Intr Number of interruption          3019 Long    
################################################
for x in range(0,20):
    regs = c.read_holding_registers(3000, 20)

    today=datetime.today();
    print("Date =", today)

    #seconds = time.time()
    #print("Seconds since epoch '", seconds);  
    pfpack = pack('>HH', regs[7], regs[6])
    pf = unpack('>f', pfpack)
    print("PF :", pf[0])
    
    mypack = pack('>HH', regs[9], regs[8])
    vll = unpack('>f', mypack)
    print("VLL:", vll[0])

    mypack = pack('>HH', regs[11], regs[10])
    vln = unpack('>f', mypack)
    print("VLN:", vln[0])

    mypack = pack('>HH', regs[13], regs[12])
    amp = unpack('>f', mypack)
    print("A  :", amp[0])

    mypack = pack('>HH', regs[15], regs[14])
    freq = unpack('>f', mypack)
    print("F  :", freq[0])

    va =  1.732*pf[0] * vll[0] * amp[0]/1000
    print("VA :",va)

    time.sleep(1)
    #seconds = time.time()
    #print("Seconds since epoch '", seconds);
else:
        print("Loop Exit")
        