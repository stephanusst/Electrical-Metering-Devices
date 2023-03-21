# Estimasi biaya beban  listrik selama 1 menit
# satuan adalah kwh
from electrical import power_lines
import time

waktu1, vr, vy, vb = power_lines(1)
print("VAR1:",vr)
vah1=vr*60/3600
print("VAR1 H:",vah1)
vah1rp=vah1*1480/1000
print("VAR1 H RP:",vah1rp)

time.sleep(1)
waktu2, vr, vy, vb = power_lines(2)
print("VAR2:",vr)
vah2 = vr*60/3600
print("VAR2 H:",vah2)
vah2rp=vah2*1480/1000
print("VAR2 H RP:",vah2rp)
