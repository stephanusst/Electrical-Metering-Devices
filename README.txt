MODULES
= electrical.py
Functions
- phase_RMS_Block(an_id, an_address) 
  ...
  return va
  Membaca data 1 buah block dan menghitung daya 1 phase
  * an_id adalah alamat modbus (1 atau 2)
  * an_address adalah DM6200 Schneider Block (3030/3060/3090) 
- power_lines(an_id):
  ...
  return today, vr, vy, vb
  Membaca data RYB dari semua block dan menghitung daya ketiga phase
  * an_id adalah alamat modbus (1 atau 2)
- line_phase(an_id, an_address):
  ...
  Membaca line phase angle block
- individual(an_id)
  ...
  Percentage and unbalance load
- power_cost(va, a_time, a_cost):  
  ...
  Mengkalkulasi rupiah dari VA


MAIN PROGRAM
- baca_total_rms.py
  Baca Total RMS dan tampilkan

- baca_total_rms_cont.py
  Baca Total RMS berulang dan tampilkan

- bacaryb.py
  Baca phase RYB dan tampilkan.
  dependency: electrical.py

- datalogger-1.py
  Data logger for all phase electrical data for panel 1
  dependency: electrical.py

- datalogger-2.py
  Data logger for all phase electrical data for panel 2

- electrical.py
  Module Pembaca DM6200  
  Dibutuhkan oleh bacaryb, datalogger-x

- estimasi_biaya_semua.py
  Estimasi biaya sebulan dari bacaan sesaat dari setiap fasa dan seluruhnya
  dependency: electrical.py

- estimasi_biaya_sephase.py
  Estimasi biaya satu menit dari bacaan sesaat pada satu fasa untuk kedua panel
  dependency: electrical.py

- phase_angle_percentage.py
  Nilai-nilai phase.

- setup.py
  Baca setup setting

 