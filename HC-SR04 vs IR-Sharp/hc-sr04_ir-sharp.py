import serial
import pandas as pd
import time

ser = serial.Serial('COM6', 115200, timeout=1)
header = ['time(s)', 'HC-SR04', 'IR-Sharp']
data = []
i = 1

start = time.time()
while i < 31:
    
    # read sensor
    s = ser.readline()
    
    if str(s) not in "b''":
        s_str = s.decode('utf-8')
        value = s_str.split(',')
        print(value)
        ultra = float(value[0])
        ir = float(value[1])
        total = [i, ultra, ir]
        data.append(total)
        
        i += 1

ser.close()
end = time.time()
t = end-start
print(t)

data = pd.DataFrame(data, columns=header)
data.to_csv('data_2.csv', index=False)
