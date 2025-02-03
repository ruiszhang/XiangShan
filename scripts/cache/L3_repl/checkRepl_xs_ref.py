#!/bin/python3
import sqlite3
import matplotlib.pyplot as plt
import numpy as np

# read xs_repl_db
conn1 = sqlite3.connect('/nfs/home/zhangruisi/Downloads/xs-env/buildfile/2023-11-30@16:32:32.db')
cursor1 = conn1.cursor()

cursor1.execute('SELECT ID, WAYCNT_0, WAYCNT_1, WAYCNT_2, WAYCNT_3, WAYCNT_4, WAYCNT_5, WAYCNT_6, WAYCNT_7, WAYCNT_8, WAYCNT_9, WAYCNT_10, WAYCNT_11, WAYCNT_12, WAYCNT_13, WAYCNT_14, WAYCNT_15, HIT, SITE, STAMP FROM l3_repl')
data1 = cursor1.fetchall()

conn1.close()

# read xs_base_db
conn2 = sqlite3.connect('/nfs/home/zhangruisi/myXiangShan/xs-env/buildfile/2023-11-30@11:38:42.db')
cursor2 = conn2.cursor()

cursor2.execute('SELECT ID, WAYCNT_0, WAYCNT_1, WAYCNT_2, WAYCNT_3, WAYCNT_4, WAYCNT_5, WAYCNT_6, WAYCNT_7, WAYCNT_8, WAYCNT_9, WAYCNT_10, WAYCNT_11, WAYCNT_12, WAYCNT_13, WAYCNT_14, WAYCNT_15, HIT, SITE, STAMP FROM l3_repl')
data2 = cursor2.fetchall()

conn2.close()

# -----------------------------------------------------------data processing--------------------------------------------------------- #

data1_np = np.array(data1)
data2_np = np.array(data2)

data1_I = data1_np[2474649:]
data2_I = data2_np[2460539:]


data1_I[:, 0] -= 2474650
data1_I[:, 1] -= 74785
data1_I[:, 2] -= 38479
data1_I[:, 3] -= 45569
data1_I[:, 4] -= 31840
data1_I[:, 5] -= 48527
data1_I[:, 6] -= 31005
data1_I[:, 7] -= 24300
data1_I[:, 8] -= 38679
data1_I[:, 9] -= 31197
data1_I[:, 10] -= 39666
data1_I[:, 11] -= 30353
data1_I[:, 12] -= 45678
data1_I[:, 13] -= 25986
data1_I[:, 14] -= 45385
data1_I[:, 15] -= 24633
data1_I[:, 16] -= 41951
data1_I[:, 19] -= 11129696

data2_I[:, 0] -= 2460540
data2_I[:, 1] -= 44346
data2_I[:, 2] -= 39386
data2_I[:, 3] -= 33395
data2_I[:, 4] -= 35879
data2_I[:, 5] -= 47721
data2_I[:, 6] -= 44764
data2_I[:, 7] -= 36123
data2_I[:, 8] -= 48529
data2_I[:, 9] -= 31393
data2_I[:, 10] -= 47762
data2_I[:, 11] -= 34063
data2_I[:, 12] -= 43438
data2_I[:, 13] -= 27016
data2_I[:, 14] -= 38212
data2_I[:, 15] -= 28532
data2_I[:, 16] -= 35403
data2_I[:, 19] -= 11036436

data1_I_slice0 = data1_I[data1_I[:, 18] == 'L3_repl_Directory_4.sliceId: Wire[UInt]']
data1_I_slice1 = data1_I[data1_I[:, 18] == 'L3_repl_Directory_5.sliceId: Wire[UInt]']
data1_I_slice2 = data1_I[data1_I[:, 18] == 'L3_repl_Directory_6.sliceId: Wire[UInt]']
data1_I_slice3 = data1_I[data1_I[:, 18] == 'L3_repl_Directory_7.sliceId: Wire[UInt]']

data2_I_slice0 = data2_I[data2_I[:, 18] == 'L3_repl_Directory_4.sliceId: Wire[UInt]']
data2_I_slice1 = data2_I[data2_I[:, 18] == 'L3_repl_Directory_5.sliceId: Wire[UInt]']
data2_I_slice2 = data2_I[data2_I[:, 18] == 'L3_repl_Directory_6.sliceId: Wire[UInt]']
data2_I_slice3 = data2_I[data2_I[:, 18] == 'L3_repl_Directory_7.sliceId: Wire[UInt]']


# -----------------------------------------------------------slice0: data processing and draw--------------------------------------------------------- #

data1_slice0_t = np.array([row[0] for row in data1_I_slice0])
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



data1_t = np.array([row[0] for row in data1])[10:]
data1_x1 = np.array([row[1] for row in data1])[10:]
data1_x2 = np.array([row[2] for row in data1])[10:]
data1_x3 = np.array([row[3] for row in data1])[10:]
data1_x4 = np.array([row[4] for row in data1])[10:]
data1_x5 = np.array([row[5] for row in data1])[10:]
data1_x6 = np.array([row[6] for row in data1])[10:]
data1_x7 = np.array([row[7] for row in data1])[10:]
data1_x8 = np.array([row[8] for row in data1])[10:]
data1_x9 = np.array([row[9] for row in data1])[10:]
data1_x10 = np.array([row[10] for row in data1])[10:]
data1_x11 = np.array([row[11] for row in data1])[10:]
data1_x12 = np.array([row[12] for row in data1])[10:]
data1_x13 = np.array([row[13] for row in data1])[10:]
data1_x14 = np.array([row[14] for row in data1])[10:]
data1_x15 = np.array([row[15] for row in data1])[10:]
data1_x16 = np.array([row[16] for row in data1])[10:]

# selected_columns = [18, 19, 0, 1-16, 17] # Site, Stamp, ID, WayCnt, Hit
data1_site_t = data1_np[:, [18, 0]]
data1_site_x1 = data1_np[:, [18, 1]]
data1_site_x2 = data1_np[:, [18, 2]]
data1_site_x3 = data1_np[:, [18, 3]]
data1_site_x4 = data1_np[:, [18, 4]]
data1_site_x5 = data1_np[:, [18, 5]]
data1_site_x6 = data1_np[:, [18, 6]]
data1_site_x7 = data1_np[:, [18, 7]]
data1_site_x8 = data1_np[:, [18, 8]]
data1_site_x9 = data1_np[:, [18, 9]]
data1_site_x10 = data1_np[:, [18, 10]]
data1_site_x11 = data1_np[:, [18, 11]]
data1_site_x12 = data1_np[:, [18, 12]]
data1_site_x13 = data1_np[:, [18, 13]]
data1_site_x14 = data1_np[:, [18, 14]]
data1_site_x15 = data1_np[:, [18, 15]]
data1_site_x16 = data1_np[:, [18, 16]]

# data1_hit = np.array([row[17] for row in data1])[10:]
# cumulative_sum1 = 0
# data1_hitSum = []
# for num in data1_hit:
#     cumulative_sum1 += num
#     data1_hitSum.append(cumulative_sum1)


# data1_sum = data1_x1 + data1_x2 + data1_x3 + data1_x4 + data1_x5 + data1_x6 + data1_x7 + data1_x8 + data1_x9 + data1_x10 + data1_x11 + data1_x12 + data1_x13 + data1_x14 + data1_x15 + data1_x16

# data1_x1_new = data1_x1 / data1_sum
# data1_x2_new = data1_x2 / data1_sum
# data1_x3_new = data1_x3 / data1_sum
# data1_x4_new = data1_x4 / data1_sum
# data1_x5_new = data1_x5 / data1_sum
# data1_x6_new = data1_x6 / data1_sum
# data1_x7_new = data1_x7 / data1_sum
# data1_x8_new = data1_x8 / data1_sum
# data1_x9_new = data1_x9 / data1_sum
# data1_x10_new = data1_x10 / data1_sum
# data1_x11_new = data1_x11 / data1_sum
# data1_x12_new = data1_x12 / data1_sum
# data1_x13_new = data1_x13 / data1_sum
# data1_x14_new = data1_x14 / data1_sum
# data1_x15_new = data1_x15 / data1_sum
# data1_x16_new = data1_x16 / data1_sum

# data1_hitRate = data1_hitSum / data1_t

# data2



data2_t = np.array([row[0] for row in data2])[10:]

data2_x1 = np.array([row[1] for row in data2])[10:]
data2_x2 = np.array([row[2] for row in data2])[10:]
data2_x3 = np.array([row[3] for row in data2])[10:]
data2_x4 = np.array([row[4] for row in data2])[10:]
data2_x5 = np.array([row[5] for row in data2])[10:]
data2_x6 = np.array([row[6] for row in data2])[10:]
data2_x7 = np.array([row[7] for row in data2])[10:]
data2_x8 = np.array([row[8] for row in data2])[10:]
data2_x9 = np.array([row[9] for row in data2])[10:]
data2_x10 = np.array([row[10] for row in data2])[10:]
data2_x11 = np.array([row[11] for row in data2])[10:]
data2_x12 = np.array([row[12] for row in data2])[10:]
data2_x13 = np.array([row[13] for row in data2])[10:]
data2_x14 = np.array([row[14] for row in data2])[10:]
data2_x15 = np.array([row[15] for row in data2])[10:]
data2_x16 = np.array([row[16] for row in data2])[10:]

# data2_hit = np.array([row[17] for row in data2])[10:]
# cumulative_sum2 = 0
# data2_hitSum = []
# for num in data2_hit:
#     cumulative_sum2 += num
#     data2_hitSum.append(cumulative_sum2)

# data2_sum = data2_x1 + data2_x2 + data2_x3 + data2_x4 + data2_x5 + data2_x6 + data2_x7 + data2_x8 + data2_x9 + data2_x10 + data2_x11 + data2_x12 + data2_x13 + data2_x14 + data2_x15 + data2_x16

# data2_x1_new = data2_x1 / data2_sum
# data2_x2_new = data2_x2 / data2_sum
# data2_x3_new = data2_x3 / data2_sum
# data2_x4_new = data2_x4 / data2_sum
# data2_x5_new = data2_x5 / data2_sum
# data2_x6_new = data2_x6 / data2_sum
# data2_x7_new = data2_x7 / data2_sum
# data2_x8_new = data2_x8 / data2_sum
# data2_x9_new = data2_x9 / data2_sum
# data2_x10_new = data2_x10 / data2_sum
# data2_x11_new = data2_x11 / data2_sum
# data2_x12_new = data2_x12 / data2_sum
# data2_x13_new = data2_x13 / data2_sum
# data2_x14_new = data2_x14 / data2_sum
# data2_x15_new = data2_x15 / data2_sum
# data2_x16_new = data2_x16 / data2_sum

# data2_hitRate = data2_hitSum / data2_t

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


