#!/bin/python3
import sqlite3
import matplotlib.pyplot as plt
import numpy as np

# read xs_repl_db
conn1 = sqlite3.connect('/nfs/home/zhangruisi/Downloads/xs-env/buildfile/2023-12-11@22:45:42.db')
cursor1 = conn1.cursor()

cursor1.execute('SELECT ID, WAYCNT_0, WAYCNT_1, WAYCNT_2, WAYCNT_3, WAYCNT_4, WAYCNT_5, WAYCNT_6, WAYCNT_7, WAYCNT_8, WAYCNT_9, WAYCNT_10, WAYCNT_11, WAYCNT_12, WAYCNT_13, WAYCNT_14, WAYCNT_15, STAMP, HIT, CHANNEL, SITE FROM l3_repl')
data1 = cursor1.fetchall()

conn1.close()

# read xs_base_db
conn2 = sqlite3.connect('/nfs/home/zhangruisi/myXiangShan/xs-env/buildfile/2023-12-11@16:15:00.db')
cursor2 = conn2.cursor()

cursor2.execute('SELECT ID, WAYCNT_0, WAYCNT_1, WAYCNT_2, WAYCNT_3, WAYCNT_4, WAYCNT_5, WAYCNT_6, WAYCNT_7, WAYCNT_8, WAYCNT_9, WAYCNT_10, WAYCNT_11, WAYCNT_12, WAYCNT_13, WAYCNT_14, WAYCNT_15, STAMP, HIT, CHANNEL, SITE FROM l3_repl')
data2 = cursor2.fetchall()

conn2.close()

# -----------------------------------------------------------data processing--------------------------------------------------------- #

data1_np = np.array(data1)
data2_np = np.array(data2)

# data1_I = np.array(data1_np[2474649:]) # to exclude warm-up
data1_I = np.array(data1_np)
bool1_index0 = np.array([x[20] == 'L3_repl_Directory_4.sliceId: Wire[UInt]' for x in data1_I])
bool1_index1 = np.array([x[20] == 'L3_repl_Directory_5.sliceId: Wire[UInt]' for x in data1_I])
bool1_index2 = np.array([x[20] == 'L3_repl_Directory_6.sliceId: Wire[UInt]' for x in data1_I])
bool1_index3 = np.array([x[20] == 'L3_repl_Directory_7.sliceId: Wire[UInt]' for x in data1_I])
data1_I_slice0_last = np.array(data1_I[bool1_index0])
data1_I_slice1_last = np.array(data1_I[bool1_index1])
data1_I_slice2_last = np.array(data1_I[bool1_index2])
data1_I_slice3_last = np.array(data1_I[bool1_index3])

data1_I_slice0_str = data1_I_slice0_last[:, :-1]
data1_I_slice1_str = data1_I_slice1_last[:, :-1]
data1_I_slice2_str = data1_I_slice2_last[:, :-1]
data1_I_slice3_str = data1_I_slice3_last[:, :-1]

def str_to_int(x):
    return int(x)

data1_I_slice0 = np.vectorize(str_to_int)(data1_I_slice0_str)
data1_I_slice1 = np.vectorize(str_to_int)(data1_I_slice1_str)
data1_I_slice2 = np.vectorize(str_to_int)(data1_I_slice2_str)
data1_I_slice3 = np.vectorize(str_to_int)(data1_I_slice3_str)
# data1_I_slice0_int = np.vectorize(str_to_int)(data1_I_slice0_str)
# data1_I_slice1_int = np.vectorize(str_to_int)(data1_I_slice1_str)
# data1_I_slice2_int = np.vectorize(str_to_int)(data1_I_slice2_str)
# data1_I_slice3_int = np.vectorize(str_to_int)(data1_I_slice3_str)

# data1_I_slice0_first_tuple_except_last = data1_I_slice0_int[0][:-1]
# data1_I_slice1_first_tuple_except_last = data1_I_slice1_int[0][:-1]
# data1_I_slice2_first_tuple_except_last = data1_I_slice2_int[0][:-1]
# data1_I_slice3_first_tuple_except_last = data1_I_slice3_int[0][:-1]

# data1_I_slice0 = np.array([tuple(np.array(x[:-1]) - np.array(data1_I_slice0_first_tuple_except_last)) + (x[-1],) for x in data1_I_slice0_int])
# data1_I_slice1 = np.array([tuple(np.array(x[:-1]) - np.array(data1_I_slice1_first_tuple_except_last)) + (x[-1],) for x in data1_I_slice1_int])
# data1_I_slice2 = np.array([tuple(np.array(x[:-1]) - np.array(data1_I_slice2_first_tuple_except_last)) + (x[-1],) for x in data1_I_slice2_int])
# data1_I_slice3 = np.array([tuple(np.array(x[:-1]) - np.array(data1_I_slice3_first_tuple_except_last)) + (x[-1],) for x in data1_I_slice3_int])

# data2_I = np.array(data2_np[2460539:])
data2_I = np.array(data2_np)
bool2_index0 = np.array([x[20] == 'L3_repl_Directory_4.sliceId: Wire[UInt]' for x in data2_I])
bool2_index1 = np.array([x[20] == 'L3_repl_Directory_5.sliceId: Wire[UInt]' for x in data2_I])
bool2_index2 = np.array([x[20] == 'L3_repl_Directory_6.sliceId: Wire[UInt]' for x in data2_I])
bool2_index3 = np.array([x[20] == 'L3_repl_Directory_7.sliceId: Wire[UInt]' for x in data2_I])
data2_I_slice0_last = np.array(data2_I[bool2_index0])
data2_I_slice1_last = np.array(data2_I[bool2_index1])
data2_I_slice2_last = np.array(data2_I[bool2_index2])
data2_I_slice3_last = np.array(data2_I[bool2_index3])

data2_I_slice0_str = data2_I_slice0_last[:, :-1]
data2_I_slice1_str = data2_I_slice1_last[:, :-1]
data2_I_slice2_str = data2_I_slice2_last[:, :-1]
data2_I_slice3_str = data2_I_slice3_last[:, :-1]

data2_I_slice0 = np.vectorize(str_to_int)(data2_I_slice0_str)
data2_I_slice1 = np.vectorize(str_to_int)(data2_I_slice1_str)
data2_I_slice2 = np.vectorize(str_to_int)(data2_I_slice2_str)
data2_I_slice3 = np.vectorize(str_to_int)(data2_I_slice3_str)


# data2_I_slice0_int = np.vectorize(str_to_int)(data2_I_slice0_str)
# data2_I_slice1_int = np.vectorize(str_to_int)(data2_I_slice1_str)
# data2_I_slice2_int = np.vectorize(str_to_int)(data2_I_slice2_str)
# data2_I_slice3_int = np.vectorize(str_to_int)(data2_I_slice3_str)

# data2_I_slice0_first_tuple_except_last = data2_I_slice0_int[0][:-1]
# data2_I_slice1_first_tuple_except_last = data2_I_slice1_int[0][:-1]
# data2_I_slice2_first_tuple_except_last = data2_I_slice2_int[0][:-1]
# data2_I_slice3_first_tuple_except_last = data2_I_slice3_int[0][:-1]

# data2_I_slice0 = np.array([tuple(np.array(x[:-1]) - np.array(data2_I_slice0_first_tuple_except_last)) + (x[-1],) for x in data2_I_slice0_int])
# data2_I_slice1 = np.array([tuple(np.array(x[:-1]) - np.array(data2_I_slice1_first_tuple_except_last)) + (x[-1],) for x in data2_I_slice1_int])
# data2_I_slice2 = np.array([tuple(np.array(x[:-1]) - np.array(data2_I_slice2_first_tuple_except_last)) + (x[-1],) for x in data2_I_slice2_int])
# data2_I_slice3 = np.array([tuple(np.array(x[:-1]) - np.array(data2_I_slice3_first_tuple_except_last)) + (x[-1],) for x in data2_I_slice3_int])

print('len(data1_I_slice0) = ', len(data1_I_slice0))
print('len(data1_I_slice1) = ', len(data1_I_slice1))
print('len(data1_I_slice2) = ', len(data1_I_slice2))
print('len(data1_I_slice3) = ', len(data1_I_slice3))



# # -------------------------------data processing and draw---------------------------------------- #

data1_slice0_hit = np.array([row[18] for row in data1_I_slice0])
data1_slice0_chn = np.array([row[19] for row in data1_I_slice0])
data1_slice0_Achn = (data1_slice0_chn == 0).astype(int)
cum0 = 0
Sum0 = []
for num in data1_slice0_Achn:
    cum0 += num
    Sum0.append(cum0)
print('data1_slice0_Achn_num = ', Sum0[-1])
data1_slice0_Ahit = (data1_slice0_hit == 1) & (data1_slice0_chn == 0)
cumulative_slice0_sum1 = 0
data1_slice0_hitSum = []
for num in data1_slice0_Ahit:
    cumulative_slice0_sum1 += num
    data1_slice0_hitSum.append(cumulative_slice0_sum1)

data1_slice1_hit = np.array([row[18] for row in data1_I_slice1])
data1_slice1_chn = np.array([row[19] for row in data1_I_slice1])
data1_slice1_Achn = (data1_slice1_chn == 0).astype(int)
cum1 = 0
Sum1 = []
for num in data1_slice1_Achn:
    cum1 += num
    Sum1.append(cum0)
print('data1_slice1_Achn_num = ', Sum1[-1])
data1_slice1_Ahit = (data1_slice1_hit == 1) & (data1_slice1_chn == 0)
cumulative_slice1_sum1 = 0
data1_slice1_hitSum = []
for num in data1_slice1_Ahit:
    cumulative_slice1_sum1 += num
    data1_slice1_hitSum.append(cumulative_slice1_sum1)

data1_slice2_hit = np.array([row[18] for row in data1_I_slice2])
data1_slice2_chn = np.array([row[19] for row in data1_I_slice2])
data1_slice2_Achn = (data1_slice2_chn == 0).astype(int)
cum2 = 0
Sum2 = []
for num in data1_slice2_Achn:
    cum2 += num
    Sum2.append(cum2)
print('data1_slice2_Achn_num = ', Sum2[-1])
data1_slice2_Ahit = (data1_slice2_hit == 1) & (data1_slice2_chn == 0)
cumulative_slice2_sum1 = 0
data1_slice2_hitSum = []
for num in data1_slice2_Ahit:
    cumulative_slice2_sum1 += num
    data1_slice2_hitSum.append(cumulative_slice2_sum1)

data1_slice3_hit = np.array([row[18] for row in data1_I_slice3])
data1_slice3_chn = np.array([row[19] for row in data1_I_slice3])
data1_slice3_Achn = (data1_slice3_chn == 0).astype(int)
cum3 = 0
Sum3 = []
for num in data1_slice3_Achn:
    cum3 += num
    Sum3.append(cum3)
print('data1_slice3_Achn_num = ', Sum3[-1])
data1_slice3_Ahit = (data1_slice3_hit == 1) & (data1_slice3_chn == 0)
cumulative_slice3_sum1 = 0
data1_slice3_hitSum = []
for num in data1_slice3_Ahit:
    cumulative_slice3_sum1 += num
    data1_slice3_hitSum.append(cumulative_slice3_sum1)


data2_slice0_hit = np.array([row[18] for row in data2_I_slice0])
data2_slice0_chn = np.array([row[19] for row in data2_I_slice0])
data2_slice0_Achn = (data2_slice0_chn == 0).astype(int)
cum4 = 0
Sum4 = []
for num in data2_slice0_Achn:
    cum4 += num
    Sum4.append(cum4)
print('data2_slice0_Achn_num = ', Sum4[-1])
data2_slice0_Ahit = (data2_slice0_hit == 1) & (data2_slice0_chn == 0)
cumulative_slice0_sum2 = 0
data2_slice0_hitSum = []
for num in data2_slice0_Ahit:
    cumulative_slice0_sum2 += num
    data2_slice0_hitSum.append(cumulative_slice0_sum2)

data2_slice1_hit = np.array([row[18] for row in data2_I_slice1])
data2_slice1_chn = np.array([row[19] for row in data2_I_slice1])
data2_slice1_Achn = (data2_slice1_chn == 0).astype(int)
cum5 = 0
Sum5 = []
for num in data2_slice1_Achn:
    cum5 += num
    Sum5.append(cum5)
print('data2_slice1_Achn_num = ', Sum5[-1])
data2_slice1_Ahit = (data2_slice1_hit == 1) & (data2_slice1_chn == 0)
cumulative_slice1_sum2 = 0
data2_slice1_hitSum = []
for num in data2_slice1_Ahit:
    cumulative_slice1_sum2 += num
    data2_slice1_hitSum.append(cumulative_slice1_sum2)
    
data2_slice2_hit = np.array([row[18] for row in data2_I_slice2])
data2_slice2_chn = np.array([row[19] for row in data2_I_slice2])
data2_slice2_Achn = (data2_slice2_chn == 0).astype(int)
cum6 = 0
Sum6 = []
for num in data2_slice2_Achn:
    cum6 += num
    Sum6.append(cum6)
print('data2_slice2_Achn_num = ', Sum6[-1])
data2_slice2_Ahit = (data2_slice2_hit == 1) & (data2_slice2_chn == 0)
cumulative_slice2_sum2 = 0
data2_slice2_hitSum = []
for num in data2_slice2_Ahit:
    cumulative_slice2_sum2 += num
    data2_slice2_hitSum.append(cumulative_slice2_sum2)

data2_slice3_hit = np.array([row[18] for row in data2_I_slice3])
data2_slice3_chn = np.array([row[19] for row in data2_I_slice3])
data2_slice3_Achn = (data2_slice3_chn == 0).astype(int)
cum7 = 0
Sum7 = []
for num in data2_slice3_Achn:
    cum7 += num
    Sum7.append(cum7)
print('data2_slice3_Achn_num = ', Sum7[-1])
data2_slice3_Ahit = (data2_slice3_hit == 1) & (data2_slice3_chn == 0)
cumulative_slice3_sum2 = 0
data2_slice3_hitSum = []
for num in data2_slice3_Ahit:
    cumulative_slice3_sum2 += num
    data2_slice3_hitSum.append(cumulative_slice3_sum2)



data1_slice0_hitRate = data1_slice0_hitSum[-1] / Sum0[-1]
data1_slice1_hitRate = data1_slice1_hitSum[-1] / Sum1[-1]
data1_slice2_hitRate = data1_slice2_hitSum[-1] / Sum2[-1]
data1_slice3_hitRate = data1_slice3_hitSum[-1] / Sum3[-1]
data1_hitRate = (data1_slice0_hitSum[-1] + data1_slice1_hitSum[-1] + data1_slice2_hitSum[-1] + data1_slice3_hitSum[-1]) / (Sum0[-1]+Sum1[-1]+Sum2[-1]+Sum3[-1])

print('data1_slice0_hitRate = ', data1_slice0_hitRate)
print('data1_slice1_hitRate = ', data1_slice1_hitRate)
print('data1_slice2_hitRate = ', data1_slice2_hitRate)
print('data1_slice3_hitRate = ', data1_slice3_hitRate)
print('data1_hitRate = ', data1_hitRate)
print('data1_A_num = ', Sum0[-1]+Sum1[-1]+Sum2[-1]+Sum3[-1])


data2_slice0_hitRate = data2_slice0_hitSum[-1] / Sum4[-1]
data2_slice1_hitRate = data2_slice1_hitSum[-1] / Sum5[-1]
data2_slice2_hitRate = data2_slice2_hitSum[-1] / Sum6[-1]
data2_slice3_hitRate = data2_slice3_hitSum[-1] / Sum7[-1]
data2_hitRate = (data2_slice0_hitSum[-1] + data2_slice1_hitSum[-1] + data2_slice2_hitSum[-1] + data2_slice3_hitSum[-1]) / (Sum4[-1]+Sum5[-1]+Sum6[-1]+Sum7[-1])

print('data2_slice0_hitRate = ', data2_slice0_hitRate)
print('data2_slice1_hitRate = ', data2_slice1_hitRate)
print('data2_slice2_hitRate = ', data2_slice2_hitRate)
print('data2_slice3_hitRate = ', data2_slice3_hitRate)
print('data2_A_num = ', Sum4[-1]+Sum5[-1]+Sum6[-1]+Sum7[-1])
print('data2_hitRate = ', data2_hitRate)







