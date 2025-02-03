# 用于计算1个或2个db文件的L3命中率
#!/bin/python3
import sqlite3
import sys
import matplotlib.pyplot as plt
import numpy as np

warm_up1 = 3000000  # mcf1915
warm_up2 = 3000000
warm_up3 = 1772300  # lbm

args = sys.argv
fileNumber = args[1]
fileType = args[2]
checkPoint = args[3]

if checkPoint == 'lbm':
    warm_up = 1772300
elif checkPoint == 'mcf':
    warm_up = 3000000
else:
    print("Wrong checkpoint name!")

# compare repl and base 
if fileNumber == '2':
    file1 = args[4] # repl_db
    file2 = args[5] # base_db

    # read xs_repl_db
    conn1 = sqlite3.connect(file1)
    cursor1 = conn1.cursor()

    cursor1.execute('SELECT ID, STAMP, HIT, CHANNEL FROM l3_repl_readDir')
    data1 = cursor1.fetchall()

    conn1.close()

    # read xs_base_db
    conn2 = sqlite3.connect(file2)
    cursor2 = conn2.cursor()

    cursor2.execute('SELECT ID, STAMP, HIT, CHANNEL FROM l3_repl_readDir')
    data2 = cursor2.fetchall()

    conn2.close()

    def str_to_int(x):
        return int(x)

    data1_np = np.array(data1)
    data1_str = np.array(data1_np)
    data1_all = np.vectorize(str_to_int)(data1_str)
    data1_I = np.array(data1_all[warm_up:]) # to exclude warm-up
    print('---------------------------------repl---------------------------------')
    print('reqNum in L3(exclude warm-up) = ', len(data1_I))

    data1_hit = np.array([row[2] for row in data1_I])
    data1_chn = np.array([row[3] for row in data1_I])
    data1_Achn = (data1_chn == 0).astype(int)
    data1_Cchn = (data1_chn == 2).astype(int)
    cum0 = 0
    Sum0 = []
    for num in data1_Achn:
        cum0 += num
        Sum0.append(cum0)
    print('Achn_reqNum = ', Sum0[-1])
    cum1 = 0
    Sum1 = []
    for num in data1_Cchn:
        cum1 += num
        Sum1.append(cum1)
    print('Cchn_reqNum = ', Sum1[-1])

    data1_Ahit = (data1_hit == 1) & (data1_chn == 0)
    cumulative_sum1 = 0
    data1_hitSum = []
    for num in data1_Ahit:
        cumulative_sum1 += num
        data1_hitSum.append(cumulative_sum1)

    data1_hitRate = data1_hitSum[-1] / Sum0[-1]

    print('L3 hitRate = ', data1_hitRate)
    print('warm-up = ', warm_up)
    print('last stamp in l3_repl = ', data1_I[-1])
    # print('data1 = ', data1_I[10:20])
    print('---------------------------------base---------------------------------')
    
    data2_np = np.array(data2)
    data2_str = np.array(data2_np)
    data2_all = np.vectorize(str_to_int)(data2_str)
    data2_I = np.array(data2_all[warm_up2:]) # to exclude warm-up

    print('reqNum in L3(exclude warm-up) = ', len(data2_I))
    data2_hit = np.array([row[2] for row in data2_I])
    data2_chn = np.array([row[3] for row in data2_I])
    data2_Achn = (data2_chn == 0).astype(int)
    data2_Cchn = (data2_chn == 2).astype(int)
    cum2 = 0
    Sum2 = []
    for num in data2_Achn:
        cum2 += num
        Sum2.append(cum2)
    print('Achn_reqNum = ', Sum2[-1])
    cum3 = 0
    Sum3 = []
    for num in data2_Cchn:
        cum3 += num
        Sum3.append(cum3)
    print('Cchn_reqNum = ', Sum3[-1])

    data2_Ahit = (data2_hit == 1) & (data2_chn == 0)
    cumulative_sum1 = 0
    data2_hitSum = []
    for num in data2_Ahit:
        cumulative_sum1 += num
        data2_hitSum.append(cumulative_sum1)

    data2_hitRate = data2_hitSum[-1] / Sum2[-1]

    print('L3 hitRate = ', data2_hitRate)
    print('warm-up = ', warm_up2)
    print('last stamp in l3_repl = ', data2_I[-1])

# ------------------------------------------- fileNumber is 1 ------------------------------------------ #
# calculate hitRate for single db
elif fileNumber == '1':
    file1 = args[4] # repl_db
    
    if fileType == 'repl':
        conn1 = sqlite3.connect(file1)
        cursor1 = conn1.cursor()
        cursor1.execute('SELECT ID, STAMP, HIT, CHANNEL FROM l3_repl_readDir')
        data1 = cursor1.fetchall()
        conn1.close()
    
    elif fileType == 'base':
        conn1 = sqlite3.connect(file1)
        cursor1 = conn1.cursor()
        cursor1.execute('SELECT ID, STAMP, HIT, CHANNEL FROM l3_repl')
        data1 = cursor1.fetchall()
        conn1.close()

    else:
        print("Wrong fileType! Only base or repl!")


    def str_to_int(x):
        return int(x)

    data1_np = np.array(data1)
    data1_str = np.array(data1_np)
    data1_all = np.vectorize(str_to_int)(data1_str)
    data1_I = np.array(data1_all[warm_up:]) # to exclude warm-up
    print('reqNum in L3(exclude warm-up) = ', len(data1_I))

    data1_hit = np.array([row[2] for row in data1_I])
    data1_chn = np.array([row[3] for row in data1_I])
    data1_Achn = (data1_chn == 0).astype(int)
    data1_Cchn = (data1_chn == 2).astype(int)
    cum0 = 0
    Sum0 = []
    for num in data1_Achn:
        cum0 += num
        Sum0.append(cum0)
    print('Achn_reqNum = ', Sum0[-1])
    cum1 = 0
    Sum1 = []
    for num in data1_Cchn:
        cum1 += num
        Sum1.append(cum1)
    print('Cchn_reqNum = ', Sum1[-1])

    data1_Ahit = (data1_hit == 1) & (data1_chn == 0)
    cumulative_sum1 = 0
    data1_hitSum = []
    for num in data1_Ahit:
        cumulative_sum1 += num
        data1_hitSum.append(cumulative_sum1)

    data1_hitRate = data1_hitSum[-1] / Sum0[-1]

    print('L3_hitRate = ', data1_hitRate)
    print('last stamp in l3_repl = ', data1_I[-1])
    print('warm-up = ', warm_up)
    # print('data1 = ', data1_I[10:20])

else:
    print("Wrong number for file numbers! 2 for compare and 1 for single! ")



