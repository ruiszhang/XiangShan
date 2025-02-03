# #!/bin/python3
# import sqlite3
# import matplotlib.pyplot as plt
# import numpy as np

# # read xs_repl_db
# conn1 = sqlite3.connect('/nfs/home/zhangruisi/Downloads/xs-env/buildfile/2023-11-30@16:32:32.db')
# cursor1 = conn1.cursor()

# cursor1.execute('SELECT ID, WAYCNT_0, WAYCNT_1, WAYCNT_2, WAYCNT_3, WAYCNT_4, WAYCNT_5, WAYCNT_6, WAYCNT_7, WAYCNT_8, WAYCNT_9, WAYCNT_10, WAYCNT_11, WAYCNT_12, WAYCNT_13, WAYCNT_14, WAYCNT_15, HIT, SITE, STAMP FROM l3_repl')
# data1 = cursor1.fetchall()

# conn1.close()

# # read xs_base_db
# conn2 = sqlite3.connect('/nfs/home/zhangruisi/myXiangShan/xs-env/buildfile/2023-11-30@11:38:42.db')
# cursor2 = conn2.cursor()

# cursor2.execute('SELECT ID, WAYCNT_0, WAYCNT_1, WAYCNT_2, WAYCNT_3, WAYCNT_4, WAYCNT_5, WAYCNT_6, WAYCNT_7, WAYCNT_8, WAYCNT_9, WAYCNT_10, WAYCNT_11, WAYCNT_12, WAYCNT_13, WAYCNT_14, WAYCNT_15, HIT, SITE, STAMP FROM l3_repl')
# data2 = cursor2.fetchall()

# conn2.close()

# # ---------------------------------------------draw------------------------------------------- #

# data2_np = np.array(data2)
# data2_I = data2_np[2460539:]
# # desired_tuple = data1_np[data1_np[:, 1] == n]

# data2_I_slice0 = data2_I[data2_I[:, 18] == 'L3_repl_Directory_4.sliceId: Wire[UInt]']
# print(data2_I_slice0[0:10])

# import matplotlib
# import matplotlib.pyplot as plt
# import numpy as np

# # 创建一些随机数据
# data = np.random.randn(1000)  # 生成随机的正态分布数据

# # 绘制直方图
# plt.hist(data, bins=30, edgecolor='black')  # bins表示条形的数量，edgecolor表示条形边缘颜色
# plt.xlabel('Value')  # x轴标签
# plt.ylabel('Frequency')  # y轴标签
# plt.title('Histogram Example')  # 标题
# plt.grid(True)  # 添加网格线
# plt.savefig('/nfs/home/zhangruisi/Downloads/xs-env/XiangShan/scripts/cache/test.png')

# data1_I_slice0 = [(tup[0] - 2474650, tup[1] - 74785, tup[2] - 38479, tup[3] - 45569, \
#                     tup[4] - 31840, tup[5] - 48527, tup[6] - 31005, tup[7] - 24300, \
#                     tup[8] - 38679, tup[9] - 31197, tup[10] - 39666, tup[11] - 30353, \
#                     tup[12] - 45678, tup[13] - 25986, tup[14] - 45385, tup[15] - 24633, \
#                     tup[16] - 41951, tup[17] - 11129696, *tup[18:]) for tup in data1_I_slice0]

# data1_I_slice1 = [(tup[0] - 2474650, tup[1] - 74785, tup[2] - 38479, tup[3] - 45569, \
#                     tup[4] - 31840, tup[5] - 48527, tup[6] - 31005, tup[7] - 24300, \
#                     tup[8] - 38679, tup[9] - 31197, tup[10] - 39666, tup[11] - 30353, \
#                     tup[12] - 45678, tup[13] - 25986, tup[14] - 45385, tup[15] - 24633, \
#                     tup[16] - 41951, tup[17] - 11129696, *tup[18:]) for tup in data1_I_slice1]
                
# data1_I_slice2 = [(tup[0] - 2474650, tup[1] - 74785, tup[2] - 38479, tup[3] - 45569, \
#                     tup[4] - 31840, tup[5] - 48527, tup[6] - 31005, tup[7] - 24300, \
#                     tup[8] - 38679, tup[9] - 31197, tup[10] - 39666, tup[11] - 30353, \
#                     tup[12] - 45678, tup[13] - 25986, tup[14] - 45385, tup[15] - 24633, \
#                     tup[16] - 41951, tup[17] - 11129696, *tup[18:]) for tup in data1_I_slice2]

# data1_I_slice3 = [(tup[0] - 2474650, tup[1] - 74785, tup[2] - 38479, tup[3] - 45569, \
#                     tup[4] - 31840, tup[5] - 48527, tup[6] - 31005, tup[7] - 24300, \
#                     tup[8] - 38679, tup[9] - 31197, tup[10] - 39666, tup[11] - 30353, \
#                     tup[12] - 45678, tup[13] - 25986, tup[14] - 45385, tup[15] - 24633, \
#                     tup[16] - 41951, tup[17] - 11129696, *tup[18:]) for tup in data1_I_slice3]

my_list = [
    ('apple', 10),
    ('banana', 15),
    ('orange', 20),
    ('apple', 5),
    ('grape', 8)
]

specific_value = 5

result = [tup for tup in my_list if tup[1] == specific_value]

if result:
    print("元组中第一个元素等于特定值的元组是：", result[0])
else:
    print("没有找到符合条件的元组")