# 實時呈現畫圖
import serial
import pandas as pd
import time
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import datetime

COM_PORT = "COM4"
BAUD_RATE = 115200
ser = serial.Serial(COM_PORT, BAUD_RATE)
dataset_1 = []
dataset_2 = []
timeset = []
counter = 0
figure, ax = plt.subplots(figsize=(8,6))
line1, = ax.plot(timeset, dataset_1)
print('time,temp,hum', file=open("test.csv", "w"))

try:
    while True:
        while ser.in_waiting:
            data = ser.readline().decode('utf-8')
            localtime = time.localtime()
            timenow = time.strftime("%m%d-%H%M", localtime)
            print(data, timenow)
            dataset_1.append(float(data.split(',')[1].strip().replace(')', '')))
            dataset_2.append(float(data.split(',')[0].strip().replace('(', '')))
            timeset.append(timenow)
            print(timeset[-1], dataset_1[-1], dataset_2[-1], file=open("test.csv", "a+"), sep=',')

            if counter >= 1:
                df = pd.read_csv('test.csv')
                df['time'] = pd.to_datetime(df['time'], format='%m%d-%H%M', errors='coerce')
                plt.plot(df['time'], df['temp'], 'r-')
                plt.plot(df['time'], df['hum'], 'b-')
                # plt.show(block=False)
                plt.pause(60)
            counter += 1
            
except KeyboardInterrupt:
    print(dataset_1)
    print(dataset_2)
    print(timeset)
    df = pd.DataFrame({'time': timeset, 'hum': dataset_2, 'temp': dataset_1})
    df.to_csv('./mydata.csv', index=False, encoding="utf-8")
    ser.close()
    print('再見！')
    
plt.show()