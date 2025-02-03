#!/bin/python3
import sqlite3
import matplotlib.pyplot as plt
import numpy as np

# read xs_repl_db
conn1 = sqlite3.connect('/nfs/home/zhangruisi/Downloads/xs-env/buildfile/2023-12-20@09:33:04.db')
cursor1 = conn1.cursor()

cursor1.execute('SELECT ID, WAYCNT_0, WAYCNT_1, WAYCNT_2, WAYCNT_3, WAYCNT_4, WAYCNT_5, WAYCNT_6, WAYCNT_7, WAYCNT_8, WAYCNT_9, WAYCNT_10, WAYCNT_11, WAYCNT_12, WAYCNT_13, WAYCNT_14, WAYCNT_15, STAMP, HIT, CHANNEL, SITE FROM l3_repl')
data1 = cursor1.fetchall()

conn1.close()

# read xs_base_db
conn2 = sqlite3.connect('/nfs/home/zhangruisi/Downloads/xs-env/buildfile/2023-12-20@12:28:56.db')
cursor2 = conn2.cursor()

cursor2.execute('SELECT ID, WAYCNT_0, WAYCNT_1, WAYCNT_2, WAYCNT_3, WAYCNT_4, WAYCNT_5, WAYCNT_6, WAYCNT_7, WAYCNT_8, WAYCNT_9, WAYCNT_10, WAYCNT_11, WAYCNT_12, WAYCNT_13, WAYCNT_14, WAYCNT_15, STAMP, HIT, CHANNEL, SITE FROM l3_repl')
data2 = cursor2.fetchall()

conn2.close()

# -----------------------------------------------------------data processing--------------------------------------------------------- #

data1_np = np.array(data1)
data2_np = np.array(data2)

data1_I = np.array(data1_np[2474649:])
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
data1_I_slice0_int = np.vectorize(str_to_int)(data1_I_slice0_str)
data1_I_slice1_int = np.vectorize(str_to_int)(data1_I_slice1_str)
data1_I_slice2_int = np.vectorize(str_to_int)(data1_I_slice2_str)
data1_I_slice3_int = np.vectorize(str_to_int)(data1_I_slice3_str)

data1_I_slice0_first_tuple_except_last = data1_I_slice0_int[0][:-1]
data1_I_slice1_first_tuple_except_last = data1_I_slice1_int[0][:-1]
data1_I_slice2_first_tuple_except_last = data1_I_slice2_int[0][:-1]
data1_I_slice3_first_tuple_except_last = data1_I_slice3_int[0][:-1]

data1_I_slice0 = np.array([tuple(np.array(x[:-1]) - np.array(data1_I_slice0_first_tuple_except_last)) + (x[-1],) for x in data1_I_slice0_int])
data1_I_slice1 = np.array([tuple(np.array(x[:-1]) - np.array(data1_I_slice1_first_tuple_except_last)) + (x[-1],) for x in data1_I_slice1_int])
data1_I_slice2 = np.array([tuple(np.array(x[:-1]) - np.array(data1_I_slice2_first_tuple_except_last)) + (x[-1],) for x in data1_I_slice2_int])
data1_I_slice3 = np.array([tuple(np.array(x[:-1]) - np.array(data1_I_slice3_first_tuple_except_last)) + (x[-1],) for x in data1_I_slice3_int])

data2_I = np.array(data2_np[2460539:])
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

data2_I_slice0_int = np.vectorize(str_to_int)(data2_I_slice0_str)
data2_I_slice1_int = np.vectorize(str_to_int)(data2_I_slice1_str)
data2_I_slice2_int = np.vectorize(str_to_int)(data2_I_slice2_str)
data2_I_slice3_int = np.vectorize(str_to_int)(data2_I_slice3_str)

data2_I_slice0_first_tuple_except_last = data2_I_slice0_int[0][:-1]
data2_I_slice1_first_tuple_except_last = data2_I_slice1_int[0][:-1]
data2_I_slice2_first_tuple_except_last = data2_I_slice2_int[0][:-1]
data2_I_slice3_first_tuple_except_last = data2_I_slice3_int[0][:-1]

data2_I_slice0 = np.array([tuple(np.array(x[:-1]) - np.array(data2_I_slice0_first_tuple_except_last)) + (x[-1],) for x in data2_I_slice0_int])
data2_I_slice1 = np.array([tuple(np.array(x[:-1]) - np.array(data2_I_slice1_first_tuple_except_last)) + (x[-1],) for x in data2_I_slice1_int])
data2_I_slice2 = np.array([tuple(np.array(x[:-1]) - np.array(data2_I_slice2_first_tuple_except_last)) + (x[-1],) for x in data2_I_slice2_int])
data2_I_slice3 = np.array([tuple(np.array(x[:-1]) - np.array(data2_I_slice3_first_tuple_except_last)) + (x[-1],) for x in data2_I_slice3_int])

# print(len(data2_I))
# print('data2_I = ', data2_I[0:5])
# print(len(data2_I_slice0_last))
# print('data2_I_slice0_last = ', data2_I_slice0_last[0:5])
# print(len(data2_I_slice0_str))
# print('data2_I_slice0_str = ', data2_I_slice0_str[0:5])


# print('data1_I_slice0 = ', data1_I_slice0[5:6])
# print('data1_I_slice1 = ', data1_I_slice1[5:6])
# print('data1_I_slice2 = ', data1_I_slice2[5:6])
# print('data1_I_slice3 = ', data1_I_slice3[5:6])

# print('data2_I_slice0 = ', data2_I_slice0[5:6])
# print('data2_I_slice1 = ', data2_I_slice1[5:6])
# print('data2_I_slice2 = ', data2_I_slice2[5:6])
# print('data2_I_slice3 = ', data2_I_slice3[5:6])

print('len(data1_I_slice0) = ', len(data1_I_slice0))
print('len(data1_I_slice1) = ', len(data1_I_slice1))
print('len(data1_I_slice2) = ', len(data1_I_slice2))
print('len(data1_I_slice3) = ', len(data1_I_slice3))



# # -----------------------------------------------------------slice0: data processing and draw--------------------------------------------------------- #

data1_slice0_t = np.array([row[0] for row in data1_I_slice0])
data1_slice1_t = np.array([row[0] for row in data1_I_slice1])
data1_slice2_t = np.array([row[0] for row in data1_I_slice2])
data1_slice3_t = np.array([row[0] for row in data1_I_slice3])

data1_slice0_w0 = np.array([row[1] for row in data1_I_slice0])
data1_slice0_w1 = np.array([row[2] for row in data1_I_slice0])
data1_slice0_w2 = np.array([row[3] for row in data1_I_slice0])
data1_slice0_w3 = np.array([row[4] for row in data1_I_slice0])
data1_slice0_w4 = np.array([row[5] for row in data1_I_slice0])
data1_slice0_w5 = np.array([row[6] for row in data1_I_slice0])
data1_slice0_w6 = np.array([row[7] for row in data1_I_slice0])
data1_slice0_w7 = np.array([row[8] for row in data1_I_slice0])
data1_slice0_w8 = np.array([row[9] for row in data1_I_slice0])
data1_slice0_w9 = np.array([row[10] for row in data1_I_slice0])
data1_slice0_w10 = np.array([row[11] for row in data1_I_slice0])
data1_slice0_w11 = np.array([row[12] for row in data1_I_slice0])
data1_slice0_w12 = np.array([row[13] for row in data1_I_slice0])
data1_slice0_w13 = np.array([row[14] for row in data1_I_slice0])
data1_slice0_w14 = np.array([row[15] for row in data1_I_slice0])
data1_slice0_w15 = np.array([row[16] for row in data1_I_slice0])

data2_slice0_t = np.array([row[0] for row in data2_I_slice0])
data2_slice1_t = np.array([row[0] for row in data2_I_slice1])
data2_slice2_t = np.array([row[0] for row in data2_I_slice2])
data2_slice3_t = np.array([row[0] for row in data2_I_slice3])

data2_slice0_w0 = np.array([row[1] for row in data2_I_slice0])
data2_slice0_w1 = np.array([row[2] for row in data2_I_slice0])
data2_slice0_w2 = np.array([row[3] for row in data2_I_slice0])
data2_slice0_w3 = np.array([row[4] for row in data2_I_slice0])
data2_slice0_w4 = np.array([row[5] for row in data2_I_slice0])
data2_slice0_w5 = np.array([row[6] for row in data2_I_slice0])
data2_slice0_w6 = np.array([row[7] for row in data2_I_slice0])
data2_slice0_w7 = np.array([row[8] for row in data2_I_slice0])
data2_slice0_w8 = np.array([row[9] for row in data2_I_slice0])
data2_slice0_w9 = np.array([row[10] for row in data2_I_slice0])
data2_slice0_w10 = np.array([row[11] for row in data2_I_slice0])
data2_slice0_w11 = np.array([row[12] for row in data2_I_slice0])
data2_slice0_w12 = np.array([row[13] for row in data2_I_slice0])
data2_slice0_w13 = np.array([row[14] for row in data2_I_slice0])
data2_slice0_w14 = np.array([row[15] for row in data2_I_slice0])
data2_slice0_w15 = np.array([row[16] for row in data2_I_slice0])

data1_slice0_sum = (data1_slice0_w0 + data1_slice0_w1 + data1_slice0_w2 + data1_slice0_w3 + 
                    data1_slice0_w4 + data1_slice0_w5 + data1_slice0_w6 + data1_slice0_w7 + 
                    data1_slice0_w8 + data1_slice0_w9 + data1_slice0_w10 + data1_slice0_w11 + 
                    data1_slice0_w12 + data1_slice0_w13 + data1_slice0_w14 + data1_slice0_w15)

data2_slice0_sum = (data2_slice0_w0 + data2_slice0_w1 + data2_slice0_w2 + data2_slice0_w3 + 
                    data2_slice0_w4 + data2_slice0_w5 + data2_slice0_w6 + data2_slice0_w7 + 
                    data2_slice0_w8 + data2_slice0_w9 + data2_slice0_w10 + data2_slice0_w11 + 
                    data2_slice0_w12 + data2_slice0_w13 + data2_slice0_w14 + data2_slice0_w15)

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
# data2_slice1_Achn = (data2_slice1_chn == 0).astype(int)
# cum = 0
# Sum = []
# for num in data2_slice1_Achn:
#     cum += num
#     Sum.append(cum)
# print('data2_slice1_Achn_num = ', Sum[-1])
data2_slice1_Ahit = (data2_slice1_hit == 1) & (data2_slice1_chn == 0)
# cum1 = 0
# Sum1 = []
# for num in data2_slice1_Ahit:
#     cum1 += num
#     Sum1.append(cum1)
# print('data2_slice1_Ahit_num = ', Sum1[-1])
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

# data1_slice0_w0_ratio = np.where(data1_slice0_sum != 0, data1_slice0_w0 / data1_slice0_sum, 0)
# data1_slice0_w1_ratio = np.where(data1_slice0_sum != 0, data1_slice0_w1 / data1_slice0_sum, 0)
# data1_slice0_w2_ratio = np.where(data1_slice0_sum != 0, data1_slice0_w2 / data1_slice0_sum, 0)
# data1_slice0_w3_ratio = np.where(data1_slice0_sum != 0, data1_slice0_w3 / data1_slice0_sum, 0)
# data1_slice0_w4_ratio = np.where(data1_slice0_sum != 0, data1_slice0_w4 / data1_slice0_sum, 0)
# data1_slice0_w5_ratio = np.where(data1_slice0_sum != 0, data1_slice0_w5 / data1_slice0_sum, 0)
# data1_slice0_w6_ratio = np.where(data1_slice0_sum != 0, data1_slice0_w6 / data1_slice0_sum, 0)
# data1_slice0_w7_ratio = np.where(data1_slice0_sum != 0, data1_slice0_w7 / data1_slice0_sum, 0)
# data1_slice0_w8_ratio = np.where(data1_slice0_sum != 0, data1_slice0_w8 / data1_slice0_sum, 0)
# data1_slice0_w9_ratio = np.where(data1_slice0_sum != 0, data1_slice0_w9 / data1_slice0_sum, 0)
# data1_slice0_w10_ratio = np.where(data1_slice0_sum != 0, data1_slice0_w10 / data1_slice0_sum, 0)
# data1_slice0_w11_ratio = np.where(data1_slice0_sum != 0, data1_slice0_w11 / data1_slice0_sum, 0)
# data1_slice0_w12_ratio = np.where(data1_slice0_sum != 0, data1_slice0_w12 / data1_slice0_sum, 0)
# data1_slice0_w13_ratio = np.where(data1_slice0_sum != 0, data1_slice0_w13 / data1_slice0_sum, 0)
# data1_slice0_w14_ratio = np.where(data1_slice0_sum != 0, data1_slice0_w14 / data1_slice0_sum, 0)
# data1_slice0_w15_ratio = np.where(data1_slice0_sum != 0, data1_slice0_w15 / data1_slice0_sum, 0)

data1_slice0_hitRate = data1_slice0_hitSum[-1] / Sum0[-1]
data1_slice1_hitRate = data1_slice1_hitSum[-1] / Sum1[-1]
data1_slice2_hitRate = data1_slice2_hitSum[-1] / Sum2[-1]
data1_slice3_hitRate = data1_slice3_hitSum[-1] / Sum3[-1]
data1_hitRate = (data1_slice0_hitSum[-1] + data1_slice1_hitSum[-1] + data1_slice2_hitSum[-1] + data1_slice3_hitSum[-1]) / (Sum0[-1]+Sum1[-1]+Sum2[-1]+Sum3[-1])
# print(len(data1_hitRate))
print('data1_slice0_hitRate = ', data1_slice0_hitRate)
print('data1_slice1_hitRate = ', data1_slice1_hitRate)
print('data1_slice2_hitRate = ', data1_slice2_hitRate)
print('data1_slice3_hitRate = ', data1_slice3_hitRate)
print('data1_hitRate = ', data1_hitRate)
# print('data1_hitNum = ', data1_slice0_hitSum[-1] + data1_slice1_hitSum[-1] + data1_slice2_hitSum[-1] + data1_slice3_hitSum[-1])
# print('data1_Num = ', len(data1_slice0_hitSum)+len(data1_slice1_hitSum)+len(data1_slice2_hitSum)+len(data1_slice3_hitSum))
print('data1_A_num = ', Sum0[-1]+Sum1[-1]+Sum2[-1]+Sum3[-1])

# data2_slice0_w0_ratio = np.where(data2_slice0_sum != 0, data2_slice0_w0 / data2_slice0_sum, 0)
# data2_slice0_w1_ratio = np.where(data2_slice0_sum != 0, data2_slice0_w1 / data2_slice0_sum, 0)
# data2_slice0_w2_ratio = np.where(data2_slice0_sum != 0, data2_slice0_w2 / data2_slice0_sum, 0)
# data2_slice0_w3_ratio = np.where(data2_slice0_sum != 0, data2_slice0_w3 / data2_slice0_sum, 0)
# data2_slice0_w4_ratio = np.where(data2_slice0_sum != 0, data2_slice0_w4 / data2_slice0_sum, 0)
# data2_slice0_w5_ratio = np.where(data2_slice0_sum != 0, data2_slice0_w5 / data2_slice0_sum, 0)
# data2_slice0_w6_ratio = np.where(data2_slice0_sum != 0, data2_slice0_w6 / data2_slice0_sum, 0)
# data2_slice0_w7_ratio = np.where(data2_slice0_sum != 0, data2_slice0_w7 / data2_slice0_sum, 0)
# data2_slice0_w8_ratio = np.where(data2_slice0_sum != 0, data2_slice0_w8 / data2_slice0_sum, 0)
# data2_slice0_w9_ratio = np.where(data2_slice0_sum != 0, data2_slice0_w9 / data2_slice0_sum, 0)
# data2_slice0_w10_ratio = np.where(data2_slice0_sum != 0, data2_slice0_w10 / data2_slice0_sum, 0)
# data2_slice0_w11_ratio = np.where(data2_slice0_sum != 0, data2_slice0_w11 / data2_slice0_sum, 0)
# data2_slice0_w12_ratio = np.where(data2_slice0_sum != 0, data2_slice0_w12 / data2_slice0_sum, 0)
# data2_slice0_w13_ratio = np.where(data2_slice0_sum != 0, data2_slice0_w13 / data2_slice0_sum, 0)
# data2_slice0_w14_ratio = np.where(data2_slice0_sum != 0, data2_slice0_w14 / data2_slice0_sum, 0)
# data2_slice0_w15_ratio = np.where(data2_slice0_sum != 0, data2_slice0_w15 / data2_slice0_sum, 0)

data2_slice0_hitRate = data2_slice0_hitSum[-1] / Sum4[-1]
data2_slice1_hitRate = data2_slice1_hitSum[-1] / Sum5[-1]
data2_slice2_hitRate = data2_slice2_hitSum[-1] / Sum6[-1]
data2_slice3_hitRate = data2_slice3_hitSum[-1] / Sum7[-1]
data2_hitRate = (data2_slice0_hitSum[-1] + data2_slice1_hitSum[-1] + data2_slice2_hitSum[-1] + data2_slice3_hitSum[-1]) / (Sum4[-1]+Sum5[-1]+Sum6[-1]+Sum7[-1])
# print(len(data1_hitRate))
# print(len(data1_hitRate))
print('data2_slice0_hitRate = ', data2_slice0_hitRate)
print('data2_slice1_hitRate = ', data2_slice1_hitRate)
print('data2_slice2_hitRate = ', data2_slice2_hitRate)
print('data2_slice3_hitRate = ', data2_slice3_hitRate)
print('data2_A_num = ', Sum4[-1]+Sum5[-1]+Sum6[-1]+Sum7[-1])
print('data2_hitRate = ', data2_hitRate)
# print('data2_hitNum = ', data2_slice0_hitSum[-1] + data2_slice1_hitSum[-1] + data2_slice2_hitSum[-1] + data2_slice3_hitSum[-1])
# print('data2_Num = ', len(data2_slice0_hitSum)+len(data2_slice1_hitSum)+len(data2_slice2_hitSum)+len(data2_slice3_hitSum))






# ----------------------------------------figure1---------------------------------------- #
# fig1, axs1 = plt.subplots(17, 1, figsize=(80, 30))

# data1_x_new_list = [data1_x1_new, data1_x2_new, data1_x3_new, data1_x4_new, data1_x5_new, data1_x6_new, data1_x7_new, data1_x8_new, data1_x9_new, data1_x10_new, data1_x11_new, data1_x12_new, data1_x13_new, data1_x14_new, data1_x15_new, data1_x16_new]
# data2_x_new_list = [data2_x1_new, data2_x2_new, data2_x3_new, data2_x4_new, data2_x5_new, data2_x6_new, data2_x7_new, data2_x8_new, data2_x9_new, data2_x10_new, data2_x11_new, data2_x12_new, data2_x13_new, data2_x14_new, data2_x15_new, data2_x16_new]

# axs1[0].plot(data1_t[1000:], data1_hitRate[1000:], label=f'hitRate_repl', marker='', color='red', linewidth=0.5)
# axs1[0].plot(data2_t[1000:], data2_hitRate[1000:], label=f'hitRate_base', marker='', color='blue', linewidth=0.5)
# axs1[0].set_title('hitRate')
# axs1[0].set_xticks(np.arange(min(data1_t[1000:]), max(data1_t[1000:])+1, 500000))
# axs1[0].legend()  # 显示图例
# axs1[0].grid(True)  # 显示网格线
# axs1[0].set_xlabel('t')
# axs1[0].set_ylabel('hitRate')
# axs1[0].ticklabel_format(style='plain', axis='x')

# for i in range(1,17):
#     axs1[i].plot(data1_t[1000:], data1_x_new_list[i-1][1000:], label=f'wayCnt{i-1}_repl', marker='', color='red', linewidth=0.5)
#     axs1[i].plot(data2_t[1000:], data2_x_new_list[i-1][1000:], label=f'wayCnt{i-1}_base', marker='', color='blue', linewidth=0.5)
#     axs1[i].set_title(f'wayCnt{i-1}')
#     axs1[i].set_xticks(np.arange(min(data1_t[1000:]), max(data1_t[1000:])+1, 500000))

# # axs1[0].plot(data1_t[1000:], data1_x1_new[1000:], label='wayCnt0_repl', marker='', color='red', linewidth=0.5)
# # axs1[0].plot(data2_t[1000:], data2_x1_new[1000:], label='wayCnt0_base', marker='', color='blue', linewidth=0.5)
# # axs1[0].set_title('wayCnt0')
# # axs1[0].set_xticks(np.arange(min(data1_t[1000:]), max(data1_t[1000:])+1, 500000))

# # axs1[1].plot(data1_t[1000:], data1_x2_new[1000:], label='wayCnt1_repl', marker='', color='red', linewidth=0.5)
# # axs1[1].plot(data2_t[1000:], data2_x2_new[1000:], label='wayCnt1_base', marker='', color='blue', linewidth=0.5)
# # axs1[1].set_title('wayCnt1')
# # axs1[1].set_xticks(np.arange(min(data1_t[1000:]), max(data1_t[1000:])+1, 500000))

# # axs1[2].plot(data1_t[1000:], data1_x3_new[1000:], label='wayCnt2_repl', marker='', color='red', linewidth=0.5)
# # axs1[2].plot(data2_t[1000:], data2_x3_new[1000:], label='wayCnt2_base', marker='', color='blue', linewidth=0.5)
# # axs1[2].set_title('wayCnt2')
# # axs1[2].set_xticks(np.arange(min(data1_t[1000:]), max(data1_t[1000:])+1, 500000))

# # axs1[3].plot(data1_t[1000:], data1_x4_new[1000:], label='wayCnt3_repl', marker='', color='red', linewidth=0.5)
# # axs1[3].plot(data2_t[1000:], data2_x4_new[1000:], label='wayCnt3_base', marker='', color='blue', linewidth=0.5)
# # axs1[3].set_title('wayCnt3')
# # axs1[3].set_xticks(np.arange(min(data1_t[1000:]), max(data1_t[1000:])+1, 500000))

# for ax in axs1[1:17]:
#     ax.legend()  # 显示图例
#     ax.grid(True)  # 显示网格线
#     ax.set_xlabel('t')
#     ax.set_ylabel('waycnt')
#     ax.ticklabel_format(style='plain', axis='x')

# fig1.suptitle('wayCnt distribution', y=0.98, fontsize=20)    # y is the distance from the figure
# fig1.tight_layout(rect=[0, 0.03, 1, 0.95])

# #fig1.show()
# fig1.savefig('/nfs/home/zhangruisi/Downloads/xs-env/XiangShan/scripts/cache/wayCnt_test_xs.svg')

# # ----------------------------------------figure2---------------------------------------- #

# fig2, axs2 = plt.subplots(6, 1, figsize=(60, 25))

# axs2[0].plot(data1_t[1000:500000], data1_x1_new[1000:500000], label='wayCnt0_repl', marker='', color='red', linewidth=0.5)
# axs2[0].plot(data2_t[1000:500000], data2_x1_new[1000:500000], label='wayCnt0_base', marker='', color='blue', linewidth=0.5)
# axs2[0].set_xticks(np.arange(min(data1_t[1000:500000]), max(data1_t[1000:500000])+1, 50000))

# axs2[1].plot(data1_t[500001:1000000], data1_x1_new[500001:1000000], label='wayCnt0_repl', marker='', color='red', linewidth=0.5)
# axs2[1].plot(data2_t[500001:1000000], data2_x1_new[500001:1000000], label='wayCnt0_base', marker='', color='blue', linewidth=0.5)
# axs2[1].set_xticks(np.arange(min(data1_t[500001:1000000]), max(data1_t[500001:1000000])+1, 50000))

# axs2[2].plot(data1_t[1000001:1500000], data1_x1_new[1000001:1500000], label='wayCnt0_repl', marker='', color='red', linewidth=0.5)
# axs2[2].plot(data2_t[1000001:1500000], data2_x1_new[1000001:1500000], label='wayCnt0_base', marker='', color='blue', linewidth=0.5)
# axs2[2].set_xticks(np.arange(min(data1_t[1000001:1500000]), max(data1_t[1000001:1500000])+1, 50000))

# axs2[3].plot(data1_t[1500001:2000000], data1_x1_new[1500001:2000000], label='wayCnt0_repl', marker='', color='red', linewidth=0.5)
# axs2[3].plot(data2_t[1500001:2000000], data2_x1_new[1500001:2000000], label='wayCnt0_base', marker='', color='blue', linewidth=0.5)
# axs2[3].set_xticks(np.arange(min(data1_t[1500001:2000000]), max(data1_t[1500001:2000000])+1, 50000))

# axs2[4].plot(data1_t[2000001:2500000], data1_x1_new[2000001:2500000], label='wayCnt0_repl', marker='', color='red', linewidth=0.5)
# axs2[4].plot(data2_t[2000001:2500000], data2_x1_new[2000001:2500000], label='wayCnt0_base', marker='', color='blue', linewidth=0.5)
# axs2[4].set_xticks(np.arange(min(data1_t[2000001:2500000]), max(data1_t[2000001:2500000])+1, 50000))

# axs2[5].plot(data1_t[2500001:], data1_x1_new[2500001:], label='wayCnt0_repl', marker='', color='red', linewidth=0.5)
# axs2[5].plot(data2_t[2500001:], data2_x1_new[2500001:], label='wayCnt0_base', marker='', color='blue', linewidth=0.5)
# axs2[5].set_xticks(np.arange(min(data1_t[2500001:]), max(data1_t[2500001:])+1, 50000))

# for ax in axs2:
#     ax.legend()  # 显示图例
#     ax.grid(True)  # 显示网格线
#     ax.set_xlabel('t')
#     ax.set_ylabel('waycnt')
#     ax.ticklabel_format(style='plain', axis='x')

# fig2.suptitle('wayCnt0 distribution', y=0.98, fontsize=20)
# fig2.tight_layout(rect=[0, 0.03, 1, 0.95])

# #fig2.show()
# fig2.savefig('/nfs/home/zhangruisi/Downloads/xs-env/XiangShan/scripts/cache/wayCnt0.svg')

# # ----------------------------------------figure3---------------------------------------- #

# fig3, axs3 = plt.subplots(6, 1, figsize=(60, 25))

# axs3[0].plot(data1_t[1000:500000], data1_x2_new[1000:500000], label='wayCnt0_repl', marker='', color='red', linewidth=0.5)
# axs3[0].plot(data2_t[1000:500000], data2_x2_new[1000:500000], label='wayCnt0_base', marker='', color='blue', linewidth=0.5)
# axs3[0].set_xticks(np.arange(min(data1_t[1000:500000]), max(data1_t[1000:500000])+1, 50000))

# axs3[1].plot(data1_t[500001:1000000], data1_x2_new[500001:1000000], label='wayCnt0_repl', marker='', color='red', linewidth=0.5)
# axs3[1].plot(data2_t[500001:1000000], data2_x2_new[500001:1000000], label='wayCnt0_base', marker='', color='blue', linewidth=0.5)
# axs3[1].set_xticks(np.arange(min(data1_t[500001:1000000]), max(data1_t[500001:1000000])+1, 50000))

# axs3[2].plot(data1_t[1000001:1500000], data1_x2_new[1000001:1500000], label='wayCnt0_repl', marker='', color='red', linewidth=0.5)
# axs3[2].plot(data2_t[1000001:1500000], data2_x2_new[1000001:1500000], label='wayCnt0_base', marker='', color='blue', linewidth=0.5)
# axs3[2].set_xticks(np.arange(min(data1_t[1000001:1500000]), max(data1_t[1000001:1500000])+1, 50000))

# axs3[3].plot(data1_t[1500001:2000000], data1_x2_new[1500001:2000000], label='wayCnt0_repl', marker='', color='red', linewidth=0.5)
# axs3[3].plot(data2_t[1500001:2000000], data2_x2_new[1500001:2000000], label='wayCnt0_base', marker='', color='blue', linewidth=0.5)
# axs3[3].set_xticks(np.arange(min(data1_t[1500001:2000000]), max(data1_t[1500001:2000000])+1, 50000))

# axs3[4].plot(data1_t[2000001:2500000], data1_x2_new[2000001:2500000], label='wayCnt0_repl', marker='', color='red', linewidth=0.5)
# axs3[4].plot(data2_t[2000001:2500000], data2_x2_new[2000001:2500000], label='wayCnt0_base', marker='', color='blue', linewidth=0.5)
# axs3[4].set_xticks(np.arange(min(data1_t[2000001:2500000]), max(data1_t[2000001:2500000])+1, 50000))

# axs3[5].plot(data1_t[2500001:], data1_x2_new[2500001:], label='wayCnt0_repl', marker='', color='red', linewidth=0.5)
# axs3[5].plot(data2_t[2500001:], data2_x2_new[2500001:], label='wayCnt0_base', marker='', color='blue', linewidth=0.5)
# axs3[5].set_xticks(np.arange(min(data1_t[2500001:]), max(data1_t[2500001:])+1, 50000))

# for ax in axs3:
#     ax.legend()  # 显示图例
#     ax.grid(True)  # 显示网格线
#     ax.set_xlabel('t')
#     ax.set_ylabel('waycnt')
#     ax.ticklabel_format(style='plain', axis='x')

# fig3.suptitle('wayCnt0 distribution', y=0.98, fontsize=20)
# fig3.tight_layout(rect=[0, 0.03, 1, 0.95])

# #fig2.show()
# fig3.savefig('/nfs/home/zhangruisi/Downloads/xs-env/XiangShan/scripts/cache/wayCnt1.svg')

# # ----------------------------------------figure4---------------------------------------- #

# fig4, axs4 = plt.subplots(6, 1, figsize=(60, 25))

# axs4[0].plot(data1_t[1000:500000], data1_x3_new[1000:500000], label='wayCnt0_repl', marker='', color='red', linewidth=0.5)
# axs4[0].plot(data2_t[1000:500000], data2_x3_new[1000:500000], label='wayCnt0_base', marker='', color='blue', linewidth=0.5)
# axs4[0].set_xticks(np.arange(min(data1_t[1000:500000]), max(data1_t[1000:500000])+1, 50000))

# axs4[1].plot(data1_t[500001:1000000], data1_x3_new[500001:1000000], label='wayCnt0_repl', marker='', color='red', linewidth=0.5)
# axs4[1].plot(data2_t[500001:1000000], data2_x3_new[500001:1000000], label='wayCnt0_base', marker='', color='blue', linewidth=0.5)
# axs4[1].set_xticks(np.arange(min(data1_t[500001:1000000]), max(data1_t[500001:1000000])+1, 50000))

# axs4[2].plot(data1_t[1000001:1500000], data1_x3_new[1000001:1500000], label='wayCnt0_repl', marker='', color='red', linewidth=0.5)
# axs4[2].plot(data2_t[1000001:1500000], data2_x3_new[1000001:1500000], label='wayCnt0_base', marker='', color='blue', linewidth=0.5)
# axs4[2].set_xticks(np.arange(min(data1_t[1000001:1500000]), max(data1_t[1000001:1500000])+1, 50000))

# axs4[3].plot(data1_t[1500001:2000000], data1_x3_new[1500001:2000000], label='wayCnt0_repl', marker='', color='red', linewidth=0.5)
# axs4[3].plot(data2_t[1500001:2000000], data2_x3_new[1500001:2000000], label='wayCnt0_base', marker='', color='blue', linewidth=0.5)
# axs4[3].set_xticks(np.arange(min(data1_t[1500001:2000000]), max(data1_t[1500001:2000000])+1, 50000))

# axs4[4].plot(data1_t[2000001:2500000], data1_x3_new[2000001:2500000], label='wayCnt0_repl', marker='', color='red', linewidth=0.5)
# axs4[4].plot(data2_t[2000001:2500000], data2_x3_new[2000001:2500000], label='wayCnt0_base', marker='', color='blue', linewidth=0.5)
# axs4[4].set_xticks(np.arange(min(data1_t[2000001:2500000]), max(data1_t[2000001:2500000])+1, 50000))

# axs4[5].plot(data1_t[2500001:], data1_x3_new[2500001:], label='wayCnt0_repl', marker='', color='red', linewidth=0.5)
# axs4[5].plot(data2_t[2500001:], data2_x3_new[2500001:], label='wayCnt0_base', marker='', color='blue', linewidth=0.5)
# axs4[5].set_xticks(np.arange(min(data1_t[2500001:]), max(data1_t[2500001:])+1, 50000))

# for ax in axs4:
#     ax.legend()  # 显示图例
#     ax.grid(True)  # 显示网格线
#     ax.set_xlabel('t')
#     ax.set_ylabel('waycnt')
#     ax.ticklabel_format(style='plain', axis='x')

# fig4.suptitle('wayCnt0 distribution', y=0.98, fontsize=20)
# fig4.tight_layout(rect=[0, 0.03, 1, 0.95])

# #fig2.show()
# fig4.savefig('/nfs/home/zhangruisi/Downloads/xs-env/XiangShan/scripts/cache/wayCnt2.svg')

# # ----------------------------------------figure5---------------------------------------- #

# fig5, axs5 = plt.subplots(6, 1, figsize=(60, 25))

# axs5[0].plot(data1_t[1000:500000], data1_x4_new[1000:500000], label='wayCnt0_repl', marker='', color='red', linewidth=0.5)
# axs5[0].plot(data2_t[1000:500000], data2_x4_new[1000:500000], label='wayCnt0_base', marker='', color='blue', linewidth=0.5)
# axs5[0].set_xticks(np.arange(min(data1_t[1000:500000]), max(data1_t[1000:500000])+1, 50000))

# axs5[1].plot(data1_t[500001:1000000], data1_x4_new[500001:1000000], label='wayCnt0_repl', marker='', color='red', linewidth=0.5)
# axs5[1].plot(data2_t[500001:1000000], data2_x4_new[500001:1000000], label='wayCnt0_base', marker='', color='blue', linewidth=0.5)
# axs5[1].set_xticks(np.arange(min(data1_t[500001:1000000]), max(data1_t[500001:1000000])+1, 50000))

# axs5[2].plot(data1_t[1000001:1500000], data1_x4_new[1000001:1500000], label='wayCnt0_repl', marker='', color='red', linewidth=0.5)
# axs5[2].plot(data2_t[1000001:1500000], data2_x4_new[1000001:1500000], label='wayCnt0_base', marker='', color='blue', linewidth=0.5)
# axs5[2].set_xticks(np.arange(min(data1_t[1000001:1500000]), max(data1_t[1000001:1500000])+1, 50000))

# axs5[3].plot(data1_t[1500001:2000000], data1_x4_new[1500001:2000000], label='wayCnt0_repl', marker='', color='red', linewidth=0.5)
# axs5[3].plot(data2_t[1500001:2000000], data2_x4_new[1500001:2000000], label='wayCnt0_base', marker='', color='blue', linewidth=0.5)
# axs5[3].set_xticks(np.arange(min(data1_t[1500001:2000000]), max(data1_t[1500001:2000000])+1, 50000))

# axs5[4].plot(data1_t[2000001:2500000], data1_x4_new[2000001:2500000], label='wayCnt0_repl', marker='', color='red', linewidth=0.5)
# axs5[4].plot(data2_t[2000001:2500000], data2_x4_new[2000001:2500000], label='wayCnt0_base', marker='', color='blue', linewidth=0.5)
# axs5[4].set_xticks(np.arange(min(data1_t[2000001:2500000]), max(data1_t[2000001:2500000])+1, 50000))

# axs5[5].plot(data1_t[2500001:], data1_x4_new[2500001:], label='wayCnt0_repl', marker='', color='red', linewidth=0.5)
# axs5[5].plot(data2_t[2500001:], data2_x4_new[2500001:], label='wayCnt0_base', marker='', color='blue', linewidth=0.5)
# axs5[5].set_xticks(np.arange(min(data1_t[2500001:]), max(data1_t[2500001:])+1, 50000))

# for ax in axs5:
#     ax.legend()  # 显示图例
#     ax.grid(True)  # 显示网格线
#     ax.set_xlabel('t')
#     ax.set_ylabel('waycnt')
#     ax.ticklabel_format(style='plain', axis='x')

# fig5.suptitle('wayCnt0 distribution', y=0.98, fontsize=20)
# fig5.tight_layout(rect=[0, 0.03, 1, 0.95])

# #fig2.show()
# fig5.savefig('/nfs/home/zhangruisi/Downloads/xs-env/XiangShan/scripts/cache/wayCnt3.svg')

# # plt.figure(figsize=(30, 25))
# # plt.plot(data1_t_1000, data1_x1_new, label='wayCnt0_repl', marker='', color='red', linewidth=0.5)
# # plt.plot(data2_t_1000, data2_x1_new, label='wayCnt0_base', marker='', color='blue', linewidth=0.5)
# # plt.plot(data1_t_1000, data1_x1_1000, label='wayCnt0', marker='', color='blue', linewidth=0.5)
# # plt.plot(data1_t_1000, data1_x2_1000, label='wayCnt1', marker='', color='red', linewidth=0.5)
# # plt.plot(data1_t_1000, data1_x3_1000, label='wayCnt2', marker='', color='green', linewidth=0.5)
# # plt.plot(data1_t_1000, data1_x4_1000, label='wayCnt3', marker='', color='yellow', linewidth=0.5)

# # plt.xlabel('t')
# # plt.ylabel('wayCnt')
# # plt.title('wayCnt distribution')
# # plt.xticks(np.arange(min(data1_t_1000), max(data1_t_1000)+1, 10000))
# # plt.legend()  # 显示图例
# # plt.grid(True)  # 显示网格线
# # plt.show()
# # plt.savefig('/nfs/home/zhangruisi/Downloads/xs-env/XiangShan/scripts/cache/wayCnt.svg')


# # print('data1_x1_new = ', data1_x1_new[5000:5010])
# # print('data1_x2_new = ', data1_x2_new[5000:5010])
# # print('data1_x3_new = ', data1_x3_new[5000:5010])
# # print('data1_x4_new = ', data1_x4_new[5000:5010])
# # print('data1_x1_1000 = ', data1_x1_1000[5000:5010])
# # print('data1_x2_1000 = ', data1_x2_1000[5000:5010])
# # print('data1_x3_1000 = ', data1_x3_1000[5000:5010])
# # print('data1_x4_1000 = ', data1_x4_1000[5000:5010])
# # print('data1_x1 = ', data1_x1[5000:5010])
# # print('data1_x2 = ', data1_x2[5000:5010])
# # print('data1_x3 = ', data1_x3[5000:5010])
# # print('data1_x4 = ', data1_x4[5000:5010])


# data1_t_cnt = len(data1_t)
# print('data1_t_cnt = ', data1_t_cnt)


