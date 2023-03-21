from pyModbusTCP.client import ModbusClient
from struct import *
from datetime import datetime
import time

###################################################
# DEFINITION: MODBUS_REQUEST(AN_ID)               #
# PF   Average    PF                   3007 Float #
# VLL  Average    line to line voltage 3009 Float #
# VLN  Average    line to neutral      3011 Float #
# A    Average    current              3013 Float #
# F    Frequency, Hz                   3015 Float #
# Intr Number of interruption          3019 Long  #
#                                                 #
# INPUT:                                          #
# an_id: server number                            #
#                                                 #
# OUTPUT:                                         #
# Host 192.168.1.254 Server No:  1                #  
# Current Time = 14:29:15                         #
# Date = 2023-03-21 14:29:15.996433               #
# PF : 0.9893401265144348                         #
# VLL: 391.26629638671875                         #
# VLN: 225.89854431152344                         #
# A  : 113.34405517578125                         #
# F  : 50.075782775878906                         #
# VA : 75.99144409469714                          #
###################################################
def modbus_request(an_id):
    # TCP auto connect on first modbus request

    c = ModbusClient(host="192.168.1.254", port=502, unit_id=an_id, auto_open=True)
    print("Host 192.168.1.254 Server No: ", an_id);
    regs = c.read_holding_registers(3000, 20)

    #for i in range(2):
        #print(i)
    #if regs:
    #    print(regs)
    #else:
    #    print("read error")    

    now =datetime.now()
    current_time=now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
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
    print("VxA :",va)

        #time.sleep(1)
        #seconds = time.time()
        #print("Seconds since epoch '", seconds);
    #else:
    #    print("Loop Exit")


#Main Program
modbus_request(1)
print("");
modbus_request(2)
