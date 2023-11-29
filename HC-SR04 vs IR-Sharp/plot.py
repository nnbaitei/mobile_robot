import csv
import matplotlib.pyplot as plt

t = []
ultra = []
ir = []

with open('data.csv', 'r') as csvfile:
    header = next(csvfile)
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        t.append(int(row[0]))
        ultra.append(float(row[1]))
        ir.append(float(row[2]))
plt.plot(t, ultra, 'r', ls='dashed', marker='o', label='HC-SR04')
plt.plot(t, ir, 'g', ls='dashed', marker='*', label='Infared Sharp')
plt.title("30 cm away from the foam pad")
plt.xlabel('Time(s)')
plt.ylabel('Distance(cm)')
plt.grid()
plt.legend()
plt.show()

ultra = []
ir = []
t = []

with open('data_2.csv', 'r') as csvfile:
    header = next(csvfile)
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        t.append(int(row[0]))
        ultra.append(float(row[1]))
        ir.append(float(row[2]))


plt.plot(t, ultra, 'r', ls='dashed', marker='o', label='HC-SR04')
plt.plot(t, ir, 'g', ls='dashed', marker='*', label='Infared Sharp')
plt.title("30 cm from the wall")
plt.xlabel('Time(s)')
plt.ylabel('Distance(cm)')
plt.grid()
plt.legend()
plt.show()
