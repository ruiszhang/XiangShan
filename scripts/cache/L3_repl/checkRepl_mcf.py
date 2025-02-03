#!/bin/python3
import sqlite3
import matplotlib.pyplot as plt
import numpy as np

# read mcf_1752db
conn1 = sqlite3.connect('/nfs/home/zhangruisi/myXiangShan/xs-env/buildfile/2023-12-20@04:28:31.db')
cursor1 = conn1.cursor()

cursor1.execute('SELECT ID, STAMP, HIT, SITE FROM l3_repl')
data1 = cursor1.fetchall()

conn1.close()

# read mcf_1915db
conn2 = sqlite3.connect('/nfs/home/zhangruisi/myXiangShan/xs-env/buildfile/2023-12-20@09:18:12.db')
cursor2 = conn2.cursor()

cursor2.execute('SELECT ID, STAMP, HIT, SITE FROM l3_repl')
data2 = cursor2.fetchall()

conn2.close()

# read mcf_23136db
conn3 = sqlite3.connect('/nfs/home/zhangruisi/myXiangShan/xs-env/buildfile/2023-12-20@07:27:13.db')
cursor3 = conn3.cursor()

cursor3.execute('SELECT ID, STAMP, HIT, SITE FROM l3_repl')
data3 = cursor3.fetchall()

conn3.close()

# -----------------------------------------------------------data processing--------------------------------------------------------- #

data1_np = np.array(data1)
data2_np = np.array(data2)
data3_np = np.array(data3)



data1_I = np.array(data1_np[2166343:])
bool1_index0 = np.array([x[3] == 'L3_repl_Directory_4.sliceId: Wire[UInt]' for x in data1_I])
bool1_index1 = np.array([x[3] == 'L3_repl_Directory_5.sliceId: Wire[UInt]' for x in data1_I])
bool1_index2 = np.array([x[3] == 'L3_repl_Directory_6.sliceId: Wire[UInt]' for x in data1_I])
bool1_index3 = np.array([x[3] == 'L3_repl_Directory_7.sliceId: Wire[UInt]' for x in data1_I])
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

data2_I = np.array(data2_np[3269298:])
bool2_index0 = np.array([x[3] == 'L3_repl_Directory_4.sliceId: Wire[UInt]' for x in data2_I])
bool2_index1 = np.array([x[3] == 'L3_repl_Directory_5.sliceId: Wire[UInt]' for x in data2_I])
bool2_index2 = np.array([x[3] == 'L3_repl_Directory_6.sliceId: Wire[UInt]' for x in data2_I])
bool2_index3 = np.array([x[3] == 'L3_repl_Directory_7.sliceId: Wire[UInt]' for x in data2_I])
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

data3_I = np.array(data3_np[3419269:])
bool3_index0 = np.array([x[3] == 'L3_repl_Directory_4.sliceId: Wire[UInt]' for x in data3_I])
bool3_index1 = np.array([x[3] == 'L3_repl_Directory_5.sliceId: Wire[UInt]' for x in data3_I])
bool3_index2 = np.array([x[3] == 'L3_repl_Directory_6.sliceId: Wire[UInt]' for x in data3_I])
bool3_index3 = np.array([x[3] == 'L3_repl_Directory_7.sliceId: Wire[UInt]' for x in data3_I])
data3_I_slice0_last = np.array(data3_I[bool3_index0])
data3_I_slice1_last = np.array(data3_I[bool3_index1])
data3_I_slice2_last = np.array(data3_I[bool3_index2])
data3_I_slice3_last = np.array(data3_I[bool3_index3])

data3_I_slice0_str = data3_I_slice0_last[:, :-1]
data3_I_slice1_str = data3_I_slice1_last[:, :-1]
data3_I_slice2_str = data3_I_slice2_last[:, :-1]
data3_I_slice3_str = data3_I_slice3_last[:, :-1]

data3_I_slice0_int = np.vectorize(str_to_int)(data3_I_slice0_str)
data3_I_slice1_int = np.vectorize(str_to_int)(data3_I_slice1_str)
data3_I_slice2_int = np.vectorize(str_to_int)(data3_I_slice2_str)
data3_I_slice3_int = np.vectorize(str_to_int)(data3_I_slice3_str)

data3_I_slice0_first_tuple_except_last = data3_I_slice0_int[0][:-1]
data3_I_slice1_first_tuple_except_last = data3_I_slice1_int[0][:-1]
data3_I_slice2_first_tuple_except_last = data3_I_slice2_int[0][:-1]
data3_I_slice3_first_tuple_except_last = data3_I_slice3_int[0][:-1]

data3_I_slice0 = np.array([tuple(np.array(x[:-1]) - np.array(data3_I_slice0_first_tuple_except_last)) + (x[-1],) for x in data3_I_slice0_int])
data3_I_slice1 = np.array([tuple(np.array(x[:-1]) - np.array(data3_I_slice1_first_tuple_except_last)) + (x[-1],) for x in data3_I_slice1_int])
data3_I_slice2 = np.array([tuple(np.array(x[:-1]) - np.array(data3_I_slice2_first_tuple_except_last)) + (x[-1],) for x in data3_I_slice2_int])
data3_I_slice3 = np.array([tuple(np.array(x[:-1]) - np.array(data3_I_slice3_first_tuple_except_last)) + (x[-1],) for x in data3_I_slice3_int])


print('data1_I_slice0 = ', data1_I_slice0[5:6])
print('data1_I_slice1 = ', data1_I_slice1[5:6])
print('data1_I_slice2 = ', data1_I_slice2[5:6])
print('data1_I_slice3 = ', data1_I_slice3[5:6])

print('data2_I_slice0 = ', data2_I_slice0[5:6])
print('data2_I_slice1 = ', data2_I_slice1[5:6])
print('data2_I_slice2 = ', data2_I_slice2[5:6])
print('data2_I_slice3 = ', data2_I_slice3[5:6])

print('data3_I_slice0 = ', data3_I_slice0[5:6])
print('data3_I_slice1 = ', data3_I_slice1[5:6])
print('data3_I_slice2 = ', data3_I_slice2[5:6])
print('data3_I_slice3 = ', data3_I_slice3[5:6])

# # # -----------------------------------------------------------slice0: data processing and draw--------------------------------------------------------- #

data1_slice0_hit = np.array([row[2] for row in data1_I_slice0])
cumulative_slice0_sum1 = 0
data1_slice0_hitSum = []
for num in data1_slice0_hit:
    cumulative_slice0_sum1 += num
    data1_slice0_hitSum.append(cumulative_slice0_sum1)

data1_slice1_hit = np.array([row[2] for row in data1_I_slice1])
cumulative_slice1_sum1 = 0
data1_slice1_hitSum = []
for num in data1_slice1_hit:
    cumulative_slice1_sum1 += num
    data1_slice1_hitSum.append(cumulative_slice1_sum1)

data1_slice2_hit = np.array([row[2] for row in data1_I_slice2])
cumulative_slice2_sum1 = 0
data1_slice2_hitSum = []
for num in data1_slice2_hit:
    cumulative_slice2_sum1 += num
    data1_slice2_hitSum.append(cumulative_slice2_sum1)

data1_slice3_hit = np.array([row[2] for row in data1_I_slice3])
cumulative_slice3_sum1 = 0
data1_slice3_hitSum = []
for num in data1_slice3_hit:
    cumulative_slice3_sum1 += num
    data1_slice3_hitSum.append(cumulative_slice3_sum1)


data2_slice0_hit = np.array([row[2] for row in data2_I_slice0])
cumulative_slice0_sum2 = 0
data2_slice0_hitSum = []
for num in data2_slice0_hit:
    cumulative_slice0_sum2 += num
    data2_slice0_hitSum.append(cumulative_slice0_sum2)

data2_slice1_hit = np.array([row[2] for row in data2_I_slice1])
cumulative_slice1_sum2 = 0
data2_slice1_hitSum = []
for num in data2_slice1_hit:
    cumulative_slice1_sum2 += num
    data2_slice1_hitSum.append(cumulative_slice1_sum2)
    
data2_slice2_hit = np.array([row[2] for row in data2_I_slice2])
cumulative_slice2_sum2 = 0
data2_slice2_hitSum = []
for num in data2_slice2_hit:
    cumulative_slice2_sum2 += num
    data2_slice2_hitSum.append(cumulative_slice2_sum2)

data2_slice3_hit = np.array([row[2] for row in data2_I_slice3])
cumulative_slice3_sum2 = 0
data2_slice3_hitSum = []
for num in data2_slice3_hit:
    cumulative_slice3_sum2 += num
    data2_slice3_hitSum.append(cumulative_slice3_sum2)

data3_slice0_hit = np.array([row[2] for row in data3_I_slice0])
cumulative_slice0_sum3 = 0
data3_slice0_hitSum = []
for num in data3_slice0_hit:
    cumulative_slice0_sum3 += num
    data3_slice0_hitSum.append(cumulative_slice0_sum3)

data3_slice1_hit = np.array([row[2] for row in data3_I_slice1])
cumulative_slice1_sum3 = 0
data3_slice1_hitSum = []
for num in data3_slice1_hit:
    cumulative_slice1_sum3 += num
    data3_slice1_hitSum.append(cumulative_slice1_sum3)

data3_slice2_hit = np.array([row[2] for row in data3_I_slice2])
cumulative_slice2_sum3 = 0
data3_slice2_hitSum = []
for num in data3_slice2_hit:
    cumulative_slice2_sum3 += num
    data3_slice2_hitSum.append(cumulative_slice2_sum3)

data3_slice3_hit = np.array([row[2] for row in data3_I_slice3])
cumulative_slice3_sum3 = 0
data3_slice3_hitSum = []
for num in data3_slice3_hit:
    cumulative_slice3_sum3 += num
    data3_slice3_hitSum.append(cumulative_slice3_sum3)


data1_slice0_hitRate = data1_slice0_hitSum[-1] / len(data1_slice0_hitSum)
data1_slice1_hitRate = data1_slice1_hitSum[-1] / len(data1_slice1_hitSum)
data1_slice2_hitRate = data1_slice2_hitSum[-1] / len(data1_slice2_hitSum)
data1_slice3_hitRate = data1_slice3_hitSum[-1] / len(data1_slice3_hitSum)
# print(len(data1_hitRate))
print('data1_slice0_hitRate = ', data1_slice0_hitRate)
print('data1_slice1_hitRate = ', data1_slice1_hitRate)
print('data1_slice2_hitRate = ', data1_slice2_hitRate)
print('data1_slice3_hitRate = ', data1_slice3_hitRate)

data2_slice0_hitRate = data2_slice0_hitSum[-1] / len(data2_slice0_hitSum)
data2_slice1_hitRate = data2_slice1_hitSum[-1] / len(data2_slice1_hitSum)
data2_slice2_hitRate = data2_slice2_hitSum[-1] / len(data2_slice2_hitSum)
data2_slice3_hitRate = data2_slice3_hitSum[-1] / len(data2_slice3_hitSum)
# print(len(data1_hitRate))
print('data2_slice0_hitRate = ', data2_slice0_hitRate)
print('data2_slice1_hitRate = ', data2_slice1_hitRate)
print('data2_slice2_hitRate = ', data2_slice2_hitRate)
print('data2_slice3_hitRate = ', data2_slice3_hitRate)


data3_slice0_hitRate = data3_slice0_hitSum[-1] / len(data3_slice0_hitSum)
data3_slice1_hitRate = data3_slice1_hitSum[-1] / len(data3_slice1_hitSum)
data3_slice2_hitRate = data3_slice2_hitSum[-1] / len(data3_slice2_hitSum)
data3_slice3_hitRate = data3_slice3_hitSum[-1] / len(data3_slice3_hitSum)
# print(len(data1_hitRate))
print('data3_slice0_hitRate = ', data3_slice0_hitRate)
print('data3_slice1_hitRate = ', data3_slice1_hitRate)
print('data3_slice2_hitRate = ', data3_slice2_hitRate)
print('data3_slice3_hitRate = ', data3_slice3_hitRate)









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


