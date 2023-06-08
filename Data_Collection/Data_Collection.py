import serial  # pySerial
import time
import matplotlib.pyplot as plt
import numpy as np
import time


COM_PORT = '/dev/cu.usbserial-1410'
BAUD_RATES = 115200    # 設定傳輸速率
ser = serial.Serial(COM_PORT, BAUD_RATES)   # 初始化序列通訊埠
time.sleep(0.5)


x = np.zeros(1000)
y = np.zeros(1000)
z = np.zeros(1000)


Gestures = ['Up', 'Down', 'Left', 'Right', 'O', 'Z', 'V', 'N']
filename = './data/GestureN/'
people = 'chen_new'

try:
    i = 1000
    count = 0
    start = 1200
    end = 1350

    ser.flushInput()
    while True:  # 若收到序列資料…

        t = time.time()
        ser.flushInput()
        data = ser.readline().decode().split('/')

        while len(data) != 3:
            data = ser.readline().decode().split('/')

        
        x = np.append(x, float(data[0]))
        y = np.append(y, float(data[1]))
        z = np.append(z, float(data[2]))


        if i - start == 0:

            print("================== START ====================")
            print(f"{filename}, the {count} th ")
            print("=============================================")
            print("=============================================")
            print("=============================================")
            print("=============================================")
            print("=============================================")
            print("=============================================")
            print("=============================================")
            print("=============================================")
            print("=============================================")
            print("=============================================")
            print("=============================================")
            print("=============================================")
            print("=============================================")
            print("=============================================")
            print("=============================================")
            print("=============================================")
            print("=============================================")
        if i - end == 0:
            print("")
            print("================== END ====================")
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            np.savez(f'{filename}{people}_new_{count}.npz', x = x[start:end], y = y[start:end],
                z = z[start:end])
            count += 1
            start += 200
            end += 200

        i += 1

    ser.close()

except KeyboardInterrupt:
    ser.close()
    

