import os
import numpy as np
import matplotlib.pyplot as plt

#Gestures = ['Up', 'Down', 'Left', 'Right', 'O', 'Z', 'V', 'N']
#FILE_NUM = 10
#filepath = './data/GestureUp/'
LENGTH = 80
dirpath = './data/'
imgpath = './imgs/'
if(os.path.isdir(imgpath) == False):
    os.mkdir(imgpath)
    
#desired_dir = 'GestureV'

dirs = os.listdir(dirpath)

def normalize(signal):
    # for s in signal:
    #     # s = (s-np.mean(s))/np.sqrt(np.var(s))
    #     s = (s-np.mean(s))
    return signal - np.mean(signal)

def find_max_segment_power(signal, length):
    max_i = 0
    max_pow = -1
    for i in range(signal.shape[0] - length):
        if np.square(signal[i:i+length]).sum() > max_pow:
            max_i = i
            max_pow = np.square(signal[i:i+length]).sum()
            # print(max_i, max_pow)
        # print(i, i+length, np.square(signal[i:i+length]).sum(),  max_pow)
    return max_i
    # return signal[max_i:max_i+length], max_i




for dir in dirs:
    print(dir)
    # if dir == desired_dir:
    # print('\n')
    # print(dir)
    if(os.path.isdir(imgpath+dir) == False):
        os.mkdir(imgpath+dir)
    files = os.listdir(dirpath+dir)
    #print(files)
    for file in sorted(files):
        if len(file.split('_')) == 2:
            continue
        #print(imgpath+dir+'/'+file[:-4]+'.png')
        draw = True
        string = dirpath+dir+'/'+file
        if string.endswith('.npz'):
            data = np.load(dirpath+dir+'/'+file)
            x = data['x']
            y = data['y']
            z = data['z']
            t = np.arange(0,150)
            
                
            if draw:
                
                fig, ax = plt.subplots(3, 1, figsize=(6,8))
                x_nor = normalize(x)
                y_nor = normalize(y)
                z_nor = normalize(z)
                start_x = find_max_segment_power(x_nor, LENGTH)
                start_y = find_max_segment_power(y_nor, LENGTH)
                start_z = find_max_segment_power(z_nor, LENGTH)
                line_x, = ax[0].plot(t,x)
                ax[0].plot(t[start_x], x[start_x], 'ro') 
                ax[0].plot(t[start_x+LENGTH], x[start_x+LENGTH], 'ro') 
                line_y, = ax[1].plot(t,y)
                ax[1].plot(t[start_y], y[start_y], 'ro')
                ax[1].plot(t[start_y+LENGTH], y[start_y+LENGTH], 'ro') 
                line_z, = ax[2].plot(t,z)
                ax[2].plot(t[start_z], z[start_z], 'ro') 
                ax[2].plot(t[start_z+LENGTH], z[start_z+LENGTH], 'ro') 
                
                print(imgpath+dir+'/'+file[:-4]+'.png')
                plt.savefig(imgpath+dir+'/'+file[:-4]+'.png')
                # plt.show()
                plt.close()
        
        
        
        
        
    
