# Pembacaan daya listrik instant
from electrical import power_lines
from electrical import phase_RMS_block

import time

for x in range(0,1):
    #today, vr, vy, vb   = power_lines(1)
    vr  = phase_RMS_block(1,3030)
    vy  = phase_RMS_block(1,3060)
    vb  = phase_RMS_block(1,3090)
    time.sleep(1)
 