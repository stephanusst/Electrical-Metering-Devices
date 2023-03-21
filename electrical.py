from pyModbusTCP.client import ModbusClient
from datetime import datetime
from struct import *

#Time Length
sampling_time = 1
time_length = {
    "times": 60*60 # sampling quantities
}
######################################################
#Reading 1 phase  only                               #
#Line Neutral Electrical Measurement                 #
# phase_RMS_block(an_id, an_address)                 #
#     an_id: address of modbus                       #
#     an_address: address of the registers           #
#R/Y/B phase Block: Address 3030/3060/3090           #
######################################################
#PF   Average    PF                   30 X   7 Float #
#VLL  Average    line to line voltage 30 X   9 Float #
#VLN  Average    line to neutral      30(X+1)1 Float #
#A    Average    current              30(X+1)3 Float #
#F    Frequency, Hz                   30(X+1)5 Float #
#Intr Number of interruption          30(X+1)9 Long  #
#Return VA = VLN x ALN x PF x                        #
######################################################
def phase_RMS_block(an_id, an_address):
    # TCP auto connect on first modbus request
    c = ModbusClient(host="192.168.1.254", port=502, unit_id=an_id, auto_open=True)
    regs = c.read_holding_registers(an_address, 20)
    today=datetime.today();
    format_today=today.strftime("%H:%M:%S")
    print("Date =", format_today," Panel No: ", an_id, "Block Address: ", an_address)
    
    pfpack = pack('>HH', regs[7], regs[6])
    pf = unpack('>f', pfpack)
    format_pf="{:.2f}".format(pf[0])
    print("PF :", format_pf)

    mypack = pack('>HH', regs[9], regs[8])
    vll = unpack('>f', mypack)
    format_vll="{:.1f}".format(vll[0])
    print("VLL:", format_vll)

    mypack = pack('>HH', regs[11], regs[10])
    vln = unpack('>f', mypack)
    format_vln="{:.1f}".format(vln[0])
    print("VLN:", format_vln)

    mypack = pack('>HH', regs[13], regs[12])
    amp = unpack('>f', mypack)
    format_amp="{:.1f}".format(amp[0])
    print("A  :", format_amp)

    mypack = pack('>HH', regs[15], regs[14])
    freq = unpack('>f', mypack)
    format_freq="{:.1f}".format(freq[0])
    print("F  :", format_freq)

    va =  pf[0] * vln[0] * amp[0]
    format_va="{:.1f}".format(va)
    print("VA :",format_va)

    return va

######################################
#Reading 3 phase 3030, 3060, and 3090#
######################################
#VA=VLN x ALN x PF                   #
######################################
def power_lines(an_id):
    #TCP auto connect on first modbus request
    c = ModbusClient(host="192.168.1.254", port=502, unit_id=an_id, auto_open=True)
    today=datetime.today();
    format_today=today.strftime("%H:%M:%S")
    
    #R phase
    regs = c.read_holding_registers(3030, 20)
    
    pfpack = pack('>HH', regs[7], regs[6])
    pfr = unpack('>f', pfpack)
    format_pfr="{:.2f}".format(pfr[0])
    #print("PF :", format_pf)

    mypack = pack('>HH', regs[11], regs[10])
    vlnr = unpack('>f', mypack)
    format_vlnr="{:.1f}".format(vlnr[0])
    #print("VLN:", format_vln)

    mypack = pack('>HH', regs[13], regs[12])
    ampr = unpack('>f', mypack)
    format_ampr="{:.1f}".format(ampr[0])
    #print("A  :", format_amp)

    vr =  pfr[0] * vlnr[0] * ampr[0]
    format_vr="{:.1f}".format(vr)
    #print("VR :",format_vr)

    #Y phase
    regs = c.read_holding_registers(3060, 20)
    pfpack = pack('>HH', regs[7], regs[6])
    pfy = unpack('>f', pfpack)
    format_pfy="{:.2f}".format(pfy[0])
    #print("PF :", format_pf)

    mypack = pack('>HH', regs[11], regs[10])
    vlny = unpack('>f', mypack)
    format_vlny="{:.1f}".format(vlny[0])
    #print("VLN:", format_vln)

    mypack = pack('>HH', regs[13], regs[12])
    ampy = unpack('>f', mypack)
    format_ampy="{:.1f}".format(ampy[0])
    #print("A  :", format_amp)

    vy =  pfy[0] * vlny[0] * ampy[0]
    format_vy="{:.1f}".format(vy)
    #print("VR :",format_vr)

    #B phase
    regs = c.read_holding_registers(3090, 20)
    pfpack = pack('>HH', regs[7], regs[6])
    pfb = unpack('>f', pfpack)
    format_pfb="{:.2f}".format(pfb[0])
    #print("PF :", format_pf)

    mypack = pack('>HH', regs[11], regs[10])
    vlnb = unpack('>f', mypack)
    format_vlnb="{:.1f}".format(vlnb[0])
    #print("VLN:", format_vln)

    mypack = pack('>HH', regs[13], regs[12])
    ampb = unpack('>f', mypack)
    format_ampb="{:.1f}".format(ampb[0])
    #print("A  :", format_amp)

    vb =  pfb[0] * vlnb[0] * ampb[0]
    format_vb="{:.1f}".format(vb)
    #print("VR :",format_vr)
    
    print(format_today,",",an_id,",",format_pfr,",",format_vlnr,",",format_ampr,",",format_vr,",",format_pfy,",",format_vlny,",",format_ampy,",",format_vy,",",format_pfb,",",format_vlnb,",",format_ampb,",",format_vb)
    
    return today, vr, vy, vb   

def line_phase(an_id, an_address):
    # TCP auto connect on first modbus request
    c = ModbusClient(host="192.168.1.254", port=502, unit_id=an_id, auto_open=True)
    regs = c.read_holding_registers(an_address, 18)
    today=datetime.today();
    format_today=today.strftime("%H:%M:%S")
    print("Date =", format_today," Panel No: ", an_id, "Block Address: ", an_address)
    
    mypack = pack('>HH', regs[1], regs[0])
    nv = unpack('>f', mypack)
    format_nv="{:.2f}".format(nv[0])
    print("Neutral voltage :", format_nv)

    mypack = pack('>HH', regs[3], regs[2])
    an = unpack('>f', mypack)
    format_an="{:.1f}".format(an[0])
    print("Neutral current:", format_an)

    mypack = pack('>HH', regs[5], regs[4])
    v1 = unpack('>f', mypack)
    format_v1="{:.1f}".format(v1[0])
    print("Voltage phase angle, phase 1:", format_v1)

    mypack = pack('>HH', regs[7], regs[6])
    v2 = unpack('>f', mypack)
    format_v2="{:.1f}".format(v2[0])
    print("Voltage phase angle, phase 2:", format_v2)

    mypack = pack('>HH', regs[9], regs[8])
    v3 = unpack('>f', mypack)
    format_v3="{:.1f}".format(v3[0])
    print("Voltage phase angle, phase 3:", format_v3)

    mypack = pack('>HH', regs[11], regs[10])
    a1 = unpack('>f', mypack)
    format_a1="{:.1f}".format(a1[0])
    print("Current phase angle, phase 1:", format_a1)

    mypack = pack('>HH', regs[13], regs[12])
    a2 = unpack('>f', mypack)
    format_a2="{:.1f}".format(a2[0])
    print("Current phase angle, phase 2:", format_a2)
    
    mypack = pack('>HH', regs[15], regs[14])
    a3 = unpack('>f', mypack)
    format_a3="{:.1f}".format(a3[0])
    print("Current phase angle, phase 3:", format_a3)

    mypack = pack('>HH', regs[17], regs[16])
    rpm = unpack('>f', mypack)
    format_rpm="{:.1f}".format(rpm[0])
    print("Rotations per minute:", format_rpm)
    
######################################    
#Average Load                        #
######################################    
def individual(an_id):
    c = ModbusClient(host="192.168.1.254", port=502, unit_id=an_id, auto_open=True)

    today=datetime.today();
    format_today=today.strftime("%H:%M:%S")
    print("Date =", format_today," Panel No: ", an_id)

    regs = c.read_holding_registers(3880, 2)  
    mypack = pack('>HH', regs[1], regs[0])
    temp = unpack('>f', mypack)
    format_temp="{:.2f}".format(temp[0])
    print("%Avg Load. Average load percentage:", format_temp)
    
    regs = c.read_holding_registers(3882, 2)  
    mypack = pack('>HH', regs[1], regs[0])
    temp = unpack('>f', mypack)
    format_temp="{:.2f}".format(temp[0])
    print("%L1. Percentage of phase 1 load:", format_temp)

    regs = c.read_holding_registers(3884, 2)  
    mypack = pack('>HH', regs[1], regs[0])
    temp = unpack('>f', mypack)
    format_temp="{:.2f}".format(temp[0])
    print("%L2. Percentage of phase 2 load:", format_temp)
    
    regs = c.read_holding_registers(3886, 2)  
    mypack = pack('>HH', regs[1], regs[0])
    temp = unpack('>f', mypack)
    format_temp="{:.2f}".format(temp[0])
    print("%L3. Percentage of phase 3 load:", format_temp)
    
    regs = c.read_holding_registers(3888, 2)  
    mypack = pack('>HH', regs[1], regs[0])
    temp = unpack('>f', mypack)
    format_temp="{:.2f}".format(temp[0])
    print("Unbalanced % load:", format_temp)

    regs = c.read_holding_registers(3890, 2)  
    mypack = pack('>HH', regs[1], regs[0])
    temp = unpack('>f', mypack)
    format_temp="{:.2f}".format(temp[0])
    print("Unbalanced % voltage:", format_temp)

    regs = c.read_holding_registers(3992, 2)  
    mypack = pack('>HH', regs[1], regs[0])
    temp = unpack('>l', mypack)
    print("On hours :", temp[0])
    
    regs = c.read_holding_registers(3998, 2)  
    mypack = pack('>HH', regs[1], regs[0])
    temp = unpack('>l', mypack)
    print("Number of power interuptions :", temp[0])
    
######################################
#VA=VLN x ALN x PF x Hour x Rupiah   #
######################################
def power_cost(va, a_time, a_cost):
    vah  = va*a_time
    varp = vah*a_cost
    format_vah  ="{:,.1f}".format(vah)
    format_varp ="{:,.1f}".format(varp)
    print("VAH:", format_vah, " for ", a_time,"hour or with Rp 1480/kwh turn into Rp", format_varp)
    print(" ")
    
def setup_read(an_id):
    c = ModbusClient(host="192.168.1.254", port=502, unit_id=an_id, auto_open=True)

    today=datetime.today();
    format_today=today.strftime("%H:%M:%S")
    print("Date =", format_today," Panel No: ", an_id)

    regs = c.read_holding_registers(100, 40)  

    a_pack = pack('>HH', regs[1], regs[0])
    r = unpack('>f', a_pack)
    format_r="{:.2f}".format(r[0])    
    print("Current Primary :", format_r)
    
    a_pack = pack('>HH', regs[3], regs[2])
    r = unpack('>f', a_pack)
    format_r="{:.2f}".format(r[0])    
    print("Current Secondary :", format_r)

    a_pack = pack('>HH', regs[5], regs[4])
    r = unpack('>f', a_pack)
    format_r="{:.2f}".format(r[0])    
    print("Voltage Primary :", format_r)

    a_pack = pack('>HH', regs[7], regs[6])
    r = unpack('>f', a_pack)
    format_r="{:.2f}".format(r[0])    
    print("Voltage Secondary :", format_r)    
    
    a_pack = pack('>HH', regs[9], regs[8])
    r = unpack('>f', a_pack)
    format_r="{:.2f}".format(r[0])    
    print("System :", format_r)  
    
    a_pack = pack('>HH', regs[11], regs[10])
    r = unpack('>f', a_pack)
    format_r="{:.2f}".format(r[0])    
    print("Phase Labeling :", format_r)  

    a_pack = pack('>HH', regs[13], regs[12])
    r = unpack('>f', a_pack)
    format_r="{:.2f}".format(r[0])    
    print("VA Fn :", format_r)

    a_pack = pack('>HH', regs[21], regs[20])
    r = unpack('>f', a_pack)
    format_r="{:.2f}".format(r[0])    
    print("BAUD :", format_r)

    a_pack = pack('>HH', regs[23], regs[22])
    r = unpack('>f', a_pack)
    format_r="{:.2f}".format(r[0])    
    print("PRTY :", format_r)

    a_pack = pack('>HH', regs[25], regs[24])
    r = unpack('>f', a_pack)
    format_r="{:.2f}".format(r[0])    
    print("ID :", format_r)
                                
    a_pack = pack('>HH', regs[27], regs[26])
    r = unpack('>f', a_pack)
    format_r="{:.2f}".format(r[0])    
    print("%FS :", format_r)
                               
    a_pack = pack('>HH', regs[31], regs[30])
    r = unpack('>f', a_pack)
    format_r="{:.2f}".format(r[0])    
    print("POLE :", format_r)

    a_pack = pack('>HH', regs[33], regs[32])
    r = unpack('>f', a_pack)
    format_r="{:.2f}".format(r[0])    
    print("PASS :", format_r)

    a_pack = pack('>HH', regs[35], regs[34])
    r = unpack('>f', a_pack)
    format_r="{:.2f}".format(r[0])    
    print("135 :", format_r)
    
    a_pack = pack('>HH', regs[37], regs[36])
    r = unpack('>f', a_pack)
    format_r="{:.2f}".format(r[0])    
    print("137 :", format_r)
    
    a_pack = pack('>HH', regs[39], regs[38])
    r = unpack('>f', a_pack)
    format_r="{:.2f}".format(r[0])    
    print("139 :", format_r)
    
                                                                                                                                                                                                                                                                
