import serial
import RPi.GPIO as GPIO
import time
import sys
import select

ser = serial.Serial('/dev/ttyS0', 9600)  
GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)  

mode = 0

while True:
    # ส่ง mode ผ่าน GPIO
    GPIO.output(16, mode)
    
    if mode == 0:
        print("send mode")
        send_data = ser.write(b'Hello from Raspi;')
        time.sleep(1)
    elif mode == 1:
        print("read mode")
        received_data = ser.readline().decode('utf-8').rstrip()
        print(received_data)

    # รอรับ input จากผู้ใช้ ภายใน 5 วินาที
    rlist, _, _ = select.select([sys.stdin], [], [], 0.5)
    if rlist:
        user_input = sys.stdin.readline().strip()
        if user_input in ['0', '1']:
            mode = int(user_input)
        elif user_input == '99':
            break
