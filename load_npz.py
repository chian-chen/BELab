import numpy as np
import matplotlib.pyplot as plt

Gestures = ['Up', 'Down', 'Left', 'Right', 'O', 'Z', 'V', 'N']
FILE_NUM = 10
filepath = './data/GestureUp/'
name = 'weng'

for i in range(FILE_NUM):
    fig, ax = plt.subplots(6, 1, figsize=(6,10))
    
    data = np.load(f'./data/GestureUP/weng_{i}.npz')
    x = data['x']
    y = data['y']
    z = data['z']
    rx = data['rx']
    ry = data['ry']
    rz = data['rz']
    t = np.arange(0,150)

    line_x, = ax[0].plot(t,x)
    line_y, = ax[1].plot(t,y)
    line_z, = ax[2].plot(t,z)
    line_rx, = ax[3].plot(t,rx)
    line_ry, = ax[4].plot(t,ry)
    line_rz, = ax[5].plot(t,rz)
    plt.savefig(f'./imgs/GestureUP_{name}_{i}.png')
    # plt.show()
    
