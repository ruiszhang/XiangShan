import numpy as np

# 读取txt文件到NumPy数组
data = np.genfromtxt('trace_1core_all.txt', delimiter=',', dtype=int)

# 生成随机的0、1、2、3组成的列
random_column = np.random.randint(4, size=(data.shape[0], 1))

# 将随机列替换第三列
data[:, 2] = random_column[:, 0]

# 将更新后的数组写回txt文件
np.savetxt('trace_4core_all.txt', data, delimiter=',', fmt='%d')