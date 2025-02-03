# 将tllog形式的香山L1-L2 trace 处理为(id, stamp, coreid, channel, opcode, param, tag, set, bank)形式的txt文件
#!/bin/python3
import sqlite3
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# read xs_repl_db
conn1 = sqlite3.connect('/nfs/home/zhangruisi/Downloads/xs-env/buildfile/2023-12-06@17:30:07.db')
cursor1 = conn1.cursor()

cursor1.execute('SELECT STAMP, CHANNEL, OPCODE, PARAM, ADDRESS, SITE FROM tllog')
data1 = cursor1.fetchall()

conn1.close()

# # read xs_base_db
# conn2 = sqlite3.connect('/nfs/home/zhangruisi/Downloads/xs-env/buildfile/2023-12-20@08:02:40.db')
# cursor2 = conn2.cursor()

# cursor2.execute('SELECT ID, STAMP, HIT, CHANNEL FROM l3_repl')
# data2 = cursor2.fetchall()

# conn2.close()

# -----------------------------------------------------------data processing--------------------------------------------------------- #
def str_to_int(x):
    return int(x)

data1_np = np.array(data1)
print('len of data1_np = ', len(data1_np))
# bool1 = np.array([x[5] == ('L2_L1I_0' || 'L2_L1D_0') for x in data1_np])
bool1 = np.array([x[5] == 'L2_L1D_0' for x in data1_np])
data1_L1 = np.array(data1_np[bool1])
data1_L1_str = data1_L1[:, :-1]
data1_int = np.vectorize(str_to_int)(data1_L1_str)
print('len of data1 = ', len(data1_int))


bool2 = np.array([((x[4] < 8589934591) and ((x[1] == 0 and x[2] == 6) or (x[1] == 2 and x[2] == 7))) for x in data1_int]) # 只能用33位地址
data1_addrcut = np.array(data1_int[bool2])
print('len of data1_addrcut = ', len(data1_addrcut))

# change address to tag + set + bank
addr_array = data1_addrcut[:, 4]

addr_binary = [np.binary_repr(x) for x in addr_array]
addr_binary_33 = np.array([binary_str.zfill(33) for binary_str in addr_binary])

# print('addr_binary_33 = ', addr_binary_33[10000:10005])

tag_array = np.array([binary_str[:13] for binary_str in addr_binary_33])
set_array = np.array([binary_str[13:25] for binary_str in addr_binary_33])
bank_array = np.array([binary_str[25:27] for binary_str in addr_binary_33])

# print('tag_binary = ', tag_array[10000:10005])
# print('set_binary = ', set_array[10000:10005])
# print('bank_binary = ', bank_array[10000:10005])

trace_array = np.column_stack((data1_addrcut[:, :-1], tag_array, set_array, bank_array))
# trace_array_01 = trace_array[0:1000]

random_coreId = np.random.randint(4, size=(1000, 1))
trace_array_1core = np.insert(trace_array, 1, 0, axis=1)  # add coreId for 1-core trace
# trace_array_1core = np.insert(trace_array_01, 1, random_coreId, axis=1)  # add coreId for 4-core trace

trace_array_1core[:, 2] = np.where(trace_array_1core[:, 2] == '0', '1', np.where(trace_array_1core[:, 2] == '2', '4', trace_array_1core[:, 2]))

binary_cols = [5, 6, 7]
for col in binary_cols:
    trace_array_1core[:, col] = [int(binary_str, 2) for binary_str in trace_array_1core[:, col]]

print('len of trace_array_1core = ', len(trace_array_1core))

bool3 = np.array([x[3] == '6' for x in trace_array_1core])
bool4 = np.array([x[3] == '7' for x in trace_array_1core])

A_num = np.count_nonzero(bool3)
C_num = np.count_nonzero(bool4)

print('number of AcquireBlock = ', A_num)
print('number of ReleaseData = ', C_num)


# 删除重复的要发两拍所以有两行的releaseData的第二行

# trace_array_1core_int = np.array(trace_array_1core).astype(int)

# df = pd.DataFrame(trace_array_1core_int, columns=[f'Column{i}' for i in range(len(trace_array_1core_int[0]))])
# rows_with_7_in_col3 = df[df['Column3'] == 7].index.tolist()

# # Create a mask to keep track of rows to delete
# delete_mask = [False] * len(df)

# # For rows where Column4 equals 7, check for duplicates in other columns
# # and mark every second row of each duplicate set for deletion
# for row in rows_with_7_in_col3:
#     # Extract the current row's values (excluding Column0 and Column4)
#     current_values = df.loc[row, ['Column1', 'Column2', 'Column4', 'Column5', 'Column6', 'Column7']].tolist()
    
#     # Find all rows with the same values in these columns
#     duplicates = df[(df['Column1'] == current_values[0]) &
#                     (df['Column2'] == current_values[1]) &
#                     (df['Column4'] == current_values[2]) &
#                     (df['Column5'] == current_values[3]) &
#                     (df['Column6'] == current_values[4]) &
#                     (df['Column7'] == current_values[5]) &
#                     (df['Column3'] == 7)]
    
#     # Mark every second row in the duplicates set for deletion, skipping the first duplicate
#     for idx, duplicate_row in enumerate(duplicates.index[1:], start=0):
#         if idx % 2 == 0:  # Even rows (1-indexed, hence odd in 0-indexed Python)
#             delete_mask[duplicate_row] = True

# # Delete marked rows
# trace_array_1core_unique = df.loc[~pd.Series(delete_mask)]

# trace_array_1core_unique

# print('len of data1_addrcut_unique = ', len(trace_array_1core_unique))
# print('trace_array_1core_unique = ', trace_array_1core_unique[10000:10005])

# 添加序号
trace_1core_index = np.insert(trace_array_1core, 0, np.arange(trace_array_1core.shape[0]), axis=1)

np.savetxt('lbm_1core_all.txt', trace_1core_index, fmt='%s', delimiter=',', newline='\n')
# np.savetxt('trace_array_1core_1000.txt', trace_array_1core_unique[:1000], fmt='%s', delimiter=',', newline='\n')
# np.savetxt('trace_1core_all_0.txt', trace_1core_index[0:670000], fmt='%s', delimiter=',', newline='\n')
# np.savetxt('trace_1core_all_1.txt', trace_1core_index[670000:1340000], fmt='%s', delimiter=',', newline='\n')
# np.savetxt('trace_1core_all_2.txt', trace_1core_index[1340000:2010000], fmt='%s', delimiter=',', newline='\n')
# np.savetxt('trace_1core_all_3.txt', trace_1core_index[2010000:2680000], fmt='%s', delimiter=',', newline='\n')
# np.savetxt('trace_1core_all_4.txt', trace_1core_index[2680000:3350000], fmt='%s', delimiter=',', newline='\n')
# np.savetxt('trace_1core_all_5.txt', trace_1core_index[3350000:4020000], fmt='%s', delimiter=',', newline='\n')
# np.savetxt('trace_1core_all_6.txt', trace_1core_index[4020000:4690000], fmt='%s', delimiter=',', newline='\n')
# np.savetxt('trace_1core_all_7.txt', trace_1core_index[4690000:5360000], fmt='%s', delimiter=',', newline='\n')
# np.savetxt('trace_1core_all_8.txt', trace_1core_index[5360000:6030000], fmt='%s', delimiter=',', newline='\n')
# np.savetxt('trace_1core_all_9.txt', trace_1core_index[6030000:], fmt='%s', delimiter=',', newline='\n')



########################################################################################################

# df = pd.DataFrame(trace_array_1core, columns=[f'Column{i}' for i in range(len(trace_array_1core[0]))])
# rows_with_7_in_col3 = df[df['Column3'] == 7].index.tolist()

# # Create a mask to keep track of rows to delete
# delete_mask = [False] * len(df)

# # For rows where Column4 equals 7, check for duplicates in other columns
# # and mark every second row of each duplicate set for deletion
# for row in rows_with_7_in_col3:
#     # Extract the current row's values (excluding Column0 and Column4)
#     current_values = df.loc[row, ['Column4', 'Column5', 'Column6', 'Column7']].tolist()
    
#     # Find all rows with the same values in these columns
#     duplicates = df[(df['Column4'] == current_values[0]) &
#                     (df['Column5'] == current_values[1]) &
#                     (df['Column6'] == current_values[2]) &
#                     (df['Column3'] == 7)]
    
#     # Mark every second row in the duplicates set for deletion, skipping the first duplicate
#     for idx, duplicate_row in enumerate(duplicates.index[1:], start=0):
#         if idx % 2 == 0:  # Even rows (1-indexed, hence odd in 0-indexed Python)
#             delete_mask[duplicate_row] = True

# # Delete marked rows
# df_filtered = df.loc[~pd.Series(delete_mask)]







