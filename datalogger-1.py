#Pembacaan biaya beban  listrik yang terpakai
# satuan adalah kwh
from electrical import power_lines
import electrical
import time

akumulator1 = 0
akumulator2 = 0
times=electrical.time_length["times"]
for x in range(0,times):
    waktu, vr, vy, vb  = power_lines(1)
    akumulator1=akumulator1+abs(vr*electrical.sampling_time/3600)+abs(vy*electrical.sampling_time/3600)+abs(vb*electrical.sampling_time/3600)
    time.sleep(electrical.sampling_time)