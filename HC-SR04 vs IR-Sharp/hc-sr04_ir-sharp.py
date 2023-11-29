import serial
import pandas as pd

ser = serial.Serial('COM6', 115200, timeout=1)
header = ['HC-SR04', 'IR-Sharp']
data = []

for i in range(3):

    # read sensor
    s = ser.readline()

    s_str = s.decode('utf-8')
    value = s_str.split(',')
    ultra = float(value[0])
    ir = float(value[1])
    total = [ultra, ir]
    data.append(total)
    
    i += 1

ser.close()

data = pd.DataFrame(data, columns=header)
data.to_csv('data.csv', index=False)
