# 用于计算单个db文件的L1发请求的数量和L3处理请求的数量、命中率（无warmup）
#!/bin/python3
import sqlite3
import sys
import matplotlib.pyplot as plt
import numpy as np

args = sys.argv
fileName = args[1]
fileType = args[2]
# read l3_repl
if fileType == 'repl': 
    conn1 = sqlite3.connect(fileName)
    cursor1 = conn1.cursor()
    cursor1.execute('SELECT ID, STAMP, HIT, CHANNEL FROM l3_repl_readDir')
    data1 = cursor1.fetchall()
    conn1.close()

elif fileType == 'base':
    conn1 = sqlite3.connect(fileName)
    cursor1 = conn1.cursor()
    cursor1.execute('SELECT ID, STAMP, HIT, CHANNEL FROM l3_repl')
    data1 = cursor1.fetchall()
    conn1.close()

else:
    print("Wrong fileType! Only base or repl!")


# read tllog
conn2 = sqlite3.connect(fileName)
cursor2 = conn2.cursor()

cursor2.execute('SELECT SITE, ID, STAMP, CHANNEL, OPCODE FROM tllog')
data2 = cursor2.fetchall()

conn2.close()

# -----------------------------------------------------------data processing--------------------------------------------------------- #
def str_to_int(x):
    return int(x)

data1_np = np.array(data1)
data1_str = np.array(data1_np)
data1_all = np.vectorize(str_to_int)(data1_str)
data1_I = np.array(data1_all[1:]) # to exclude warm-up


data2_np = np.array(data2)
data2_str = np.array(data2_np)
bool1 = np.array([(x[0] == 'L2_L1_0' and (x[3] == '0' or x[3] == '2') and (x[4] == '6' or x[4] == '7'))for x in data2_str])
data2_L1_str = np.array(data2_str[bool1])
data2_L1_int = data2_L1_str[:, 1:]
data2_all = np.vectorize(str_to_int)(data2_L1_int)
data2_I = np.array(data2_all[1:]) # to exclude warm-up

# # -------------------------------data processing and draw---------------------------------------- #

data1_hit = np.array([row[2] for row in data1_I])
data1_chn = np.array([row[3] for row in data1_I])
data1_Achn = (data1_chn == 0).astype(int)
data1_Cchn = (data1_chn == 2).astype(int)
cum2 = 0
Sum2 = []
for num in data1_Achn:
    cum2 += num
    Sum2.append(cum2)

cum3 = 0
Sum3 = []
for num in data1_Cchn:
    cum3 += num
    Sum3.append(cum3)


data1_Ahit = (data1_hit == 1) & (data1_chn == 0)
cumulative_sum1 = 0
data1_hitSum = []
for num in data1_Ahit:
    cumulative_sum1 += num
    data1_hitSum.append(cumulative_sum1)

data1_hitRate = data1_hitSum[-1] / Sum2[-1]

print('')
print('-----------------------------L1 to L2-----------------------------')
print('')
print('request number from L1 to L2 in tllog = ', len(data2_I))
data2_chn = np.array([row[2] for row in data2_I])
data2_Achn = (data2_chn == 0).astype(int)
data2_Cchn = (data2_chn == 2).astype(int)
cum0 = 0
Sum0 = []
for num in data2_Achn:
    cum0 += num
    Sum0.append(cum0)
print('req_Achn_num = ', Sum0[-1])
cum1 = 0
Sum1 = []
for num in data2_Cchn:
    cum1 += num
    Sum1.append(cum1)
print('req_Cchn_num = ', Sum1[-1])

print('last = (ID,STAMP,CHANNEL,OPCODE)', data2_I[-1])
print('')
print('')

print('-----------------------------L2 to L3-----------------------------')
print('')
print('request number to L3 in l3_repl = ', len(data1_I))
print('req_Achn_num = ', Sum2[-1])
print('req_Cchn_num = ', Sum3[-1])
print('L3_hitRate(no-warm-up) = ', data1_hitRate)
print('last = (ID,STAMP,HIT,CHANNEL)', data1_I[-1])
print('')





