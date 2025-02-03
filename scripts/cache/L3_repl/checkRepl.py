#!/bin/python3
import sqlite3
import matplotlib.pyplot as plt
import numpy as np

# read tl_repl_db
conn1 = sqlite3.connect('/nfs/home/zhangruisi/Downloads/tl-test/build/2023-11-28@12:48:32.db')
cursor1 = conn1.cursor()

cursor1.execute('SELECT ID, WAYCNT_0, WAYCNT_1, WAYCNT_2, WAYCNT_3 FROM l3_repl')
data1 = cursor1.fetchall()

conn1.close()

# read tl_base_db
conn2 = sqlite3.connect('/nfs/home/zhangruisi/myXiangShan/tl-test/build/2023-11-28@17:02:35.db')
cursor2 = conn2.cursor()

cursor2.execute('SELECT ID, WAYCNT_0, WAYCNT_1, WAYCNT_2, WAYCNT_3 FROM l3_repl')
data2 = cursor2.fetchall()

conn2.close()

# ---------------------------------------------draw------------------------------------------- #

# data1
data1_np = np.array(data1)

data1_t = np.array([row[0] for row in data1])[1:]
data1_x1 = np.array([row[1] for row in data1])[1:]
data1_x2 = np.array([row[2] for row in data1])[1:]
data1_x3 = np.array([row[3] for row in data1])[1:]
data1_x4 = np.array([row[4] for row in data1])[1:]

data1_t_1000 = data1_t[1:100000]
data1_x1_1000 = data1_x1[1:100000]
data1_x2_1000 = data1_x2[1:100000]
data1_x3_1000 = data1_x3[1:100000]
data1_x4_1000 = data1_x4[1:100000]

# data1_t_x1 = data1_np[:, [0, 1]]
# data1_t_x2 = data1_np[:, [0, 2]]
# data1_t_x3 = data1_np[:, [0, 3]]
# data1_t_x4 = data1_np[:, [0, 4]]

# data1_t_sp = data1_t[::100000]
# data1_x1_sp = data1_x1[::100000]
# data1_x2_sp = data1_x2[::100000]
# data1_x3_sp = data1_x3[::100000]
# data1_x4_sp = data1_x4[::100000]

data1_sum = data1_x1 + data1_x2 + data1_x3 + data1_x4
data1_x1_new = data1_x1 / data1_sum
data1_x2_new = data1_x2 / data1_sum
data1_x3_new = data1_x3 / data1_sum
data1_x4_new = data1_x4 / data1_sum

# data2
data2_np = np.array(data2)

data2_t = np.array([row[0] for row in data2])[1:]
data2_x1 = np.array([row[1] for row in data2])[1:]
data2_x2 = np.array([row[2] for row in data2])[1:]
data2_x3 = np.array([row[3] for row in data2])[1:]
data2_x4 = np.array([row[4] for row in data2])[1:]

data2_t_1000 = data2_t[1:100000]
data2_x1_1000 = data2_x1[1:100000]
data2_x2_1000 = data2_x2[1:100000]
data2_x3_1000 = data2_x3[1:100000]
data2_x4_1000 = data2_x4[1:100000]

# data2_t_x1 = data2_np[:, [0, 1]]
# data2_t_x2 = data2_np[:, [0, 2]]
# data2_t_x3 = data2_np[:, [0, 3]]
# data2_t_x4 = data2_np[:, [0, 4]]

# data2_t_sp = data2_t[::100000]
# data2_x1_sp = data2_x1[::100000]
# data2_x2_sp = data2_x2[::100000]
# data2_x3_sp = data2_x3[::100000]
# data2_x4_sp = data2_x4[::100000]

data2_sum = data2_x1 + data2_x2 + data2_x3 + data2_x4
data2_x1_new = data2_x1 / data2_sum
data2_x2_new = data2_x2 / data2_sum
data2_x3_new = data2_x3 / data2_sum
data2_x4_new = data2_x4 / data2_sum

# ----------------------------------------figure1---------------------------------------- #
fig1, axs1 = plt.subplots(4, 1, figsize=(60, 50))

axs1[0].plot(data1_t[1000:], data1_x1_new[1000:], label='wayCnt0_repl', marker='', color='red', linewidth=0.5)
axs1[0].plot(data2_t[1000:], data2_x1_new[1000:], label='wayCnt0_base', marker='', color='blue', linewidth=0.5)
axs1[0].set_title('wayCnt0')
axs1[0].set_xticks(np.arange(min(data1_t[1000:]), max(data1_t[1000:])+1, 500000))

axs1[1].plot(data1_t[1000:], data1_x2_new[1000:], label='wayCnt1_repl', marker='', color='red', linewidth=0.5)
axs1[1].plot(data2_t[1000:], data2_x2_new[1000:], label='wayCnt1_base', marker='', color='blue', linewidth=0.5)
axs1[1].set_title('wayCnt1')
axs1[1].set_xticks(np.arange(min(data1_t[1000:]), max(data1_t[1000:])+1, 500000))

axs1[2].plot(data1_t[1000:], data1_x3_new[1000:], label='wayCnt2_repl', marker='', color='red', linewidth=0.5)
axs1[2].plot(data2_t[1000:], data2_x3_new[1000:], label='wayCnt2_base', marker='', color='blue', linewidth=0.5)
axs1[2].set_title('wayCnt2')
axs1[2].set_xticks(np.arange(min(data1_t[1000:]), max(data1_t[1000:])+1, 500000))

axs1[3].plot(data1_t[1000:], data1_x4_new[1000:], label='wayCnt3_repl', marker='', color='red', linewidth=0.5)
axs1[3].plot(data2_t[1000:], data2_x4_new[1000:], label='wayCnt3_base', marker='', color='blue', linewidth=0.5)
axs1[3].set_title('wayCnt3')
axs1[3].set_xticks(np.arange(min(data1_t[1000:]), max(data1_t[1000:])+1, 500000))

for ax in axs1:
    ax.legend()  # 显示图例
    ax.grid(True)  # 显示网格线
    ax.set_xlabel('t')
    ax.set_ylabel('waycnt')
    ax.ticklabel_format(style='plain', axis='x')

fig1.suptitle('wayCnt distribution(0-100,000)', y=0.98, fontsize=20)    # y is the distance from the figure
fig1.tight_layout(rect=[0, 0.03, 1, 0.95])

#fig1.show()
fig1.savefig('/nfs/home/zhangruisi/Downloads/xs-env/XiangShan/scripts/cache/wayCnt_full.svg')

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


