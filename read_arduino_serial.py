import serial  # 引用pySerial模組
# import pyautogui
import time
import matplotlib.pyplot as plt
import numpy as np
import time

# DATA_NUM = 200
# recording = False

COM_PORT = '/dev/cu.usbserial-1430'
BAUD_RATES = 38400    # 設定傳輸速率
ser = serial.Serial(COM_PORT, BAUD_RATES)   # 初始化序列通訊埠


# fig, ax = plt.subplots(6, 1, figsize = (8, 8))

# Set the x and y limits for each subplot
# ax[0].set_ylim([-20, 20])
# ax[1].set_ylim([-20, 20])
# ax[2].set_ylim([-20, 20])
# ax[3].set_ylim([-360, 360])
# ax[4].set_ylim([-360, 360])
# ax[5].set_ylim([-360, 360])

# Initialize the x, y, z, and t data
x = np.zeros(1000)
y = np.zeros(1000)
z = np.zeros(1000)
rx = np.zeros(1000)
ry = np.zeros(1000)
rz = np.zeros(1000)
# t = np.arange(0, 10, 0.01)



# Initialize the line objects for each subplot
# line_x, = ax[0].plot(t, x)
# line_y, = ax[1].plot(t, y)
# line_z, = ax[2].plot(t, z)
# line_rx, = ax[3].plot(t, rx)
# line_ry, = ax[4].plot(t, ry)
# line_rz, = ax[5].plot(t, rz)

Gestures = ['Up', 'Down', 'Left', 'Right', 'O', 'Z', 'V', 'N']
filename = './data/Noise/'
people = 'ko'

try:
    i = 1000
    count = 32
    start = 1200
    end = 1350

    ser.flushInput()
    while True:  # 若收到序列資料…

        # ser.write("Hello".encode())

        ser.flushInput()
        data = ser.readline().decode().split('/')

        while len(data) != 6:
            data = ser.readline().decode().split('/')

        
        x = np.append(x, float(data[0]))
        y = np.append(y, float(data[1]))
        z = np.append(z, float(data[2]))
        rx = np.append(rx, float(data[3]))
        ry = np.append(ry, float(data[4]))
        rz = np.append(rz, float(data[5]))
        # t = np.append(t, t[i-1]+0.1)

        # # # Update the line objects with the new data
        # line_x.set_data(t[i-1000:i], x[i-1000:i])
        # line_y.set_data(t[i-1000:i], y[i-1000:i])
        # line_z.set_data(t[i-1000:i], z[i-1000:i])
        # line_rx.set_data(t[i-1000:i], rx[i-1000:i])
        # line_ry.set_data(t[i-1000:i], ry[i-1000:i])
        # line_rz.set_data(t[i-1000:i], rz[i-1000:i])

        # ax[0].set_xlim([t[i]-10, t[i]])
        # ax[1].set_xlim([t[i]-10, t[i]])
        # ax[2].set_xlim([t[i]-10, t[i]])
        # ax[3].set_xlim([t[i]-10, t[i]])
        # ax[4].set_xlim([t[i]-10, t[i]])
        # ax[5].set_xlim([t[i]-10, t[i]])

        if i - start == 0:

            print("================== START ====================")
            print(f"{filename}, the {count} th ")
            
            
        if i - end == 0:
            print("")
            print("================== END ====================")
            print("\n\n\n\n\n\n\n\n\n")
            np.savez(f'{filename}{people}_{count}.npz', x = x[start:end], y = y[start:end],
                z = z[start:end], rx = rx[start:end], ry = ry[start:end], rz = rz[start:end])
            count += 1
            start += 400
            end += 400

            

        # Pause the loop for a short period of time to create a real-time animation
        # print(f'i = {i}: {data[0]}, {data[1]}, {data[2]}, {data[3]}, {data[4]}, {data[5]} | Time: {time.time() - start}')

        # plt.pause(0.001)
  
        i += 1

except KeyboardInterrupt:
    ser.close()    # 清除序列通訊物件
    




















