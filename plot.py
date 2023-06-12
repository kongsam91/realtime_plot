import pandas as pd
import matplotlib.dates as mdates    #處理日期
import matplotlib.pyplot as plt
import datetime


# 读取CSV文件
df = pd.read_csv('mydata.csv',encoding="utf-8")
# 将时间列转换为日期时间格式
df['time'] = pd.to_datetime(df['time'], format='%m%d-%H%M ')

# 创建图表
plt.plot(df['time'], df['temp'],'r-')
plt.plot(df['time'], df['hum'],'b-')


# 显示图表
plt.show()
