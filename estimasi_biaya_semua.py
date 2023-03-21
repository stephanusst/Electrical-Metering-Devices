#Pembacaan sesaat daya listrik yang terpakai beserta estimasinya
from electrical import power_cost
from electrical import phase_RMS_block
import time

def block(a_name, an_id, hours, a_cost):
    print(a_name)
    print("Average x 3")
    va = phase_RMS_block(an_id, 3000)*3
    power_cost(abs(va), hours, a_cost)
    print("R phase")
    vr = phase_RMS_block(an_id, 3030)
    power_cost(abs(vr), hours, a_cost)
    print("Y phase")
    vy = phase_RMS_block(an_id, 3060)
    power_cost(abs(vy), hours, a_cost)
    print("B phase")
    vb = phase_RMS_block(an_id, 3090)
    power_cost(abs(vb), hours, a_cost)
    total=abs(vr)+abs(vy)+abs(vb);
    format_total="{:.1f}".format(va)
    print("Total CS = ", format_total)
    power_cost(total, hours, a_cost)
    print(" ")

block("CS  ", 1, 24*30, 1480)
block("ABF ", 2, 24*30, 1480)
