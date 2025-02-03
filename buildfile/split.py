# 原始日志文件路径
input_file_path = 'chrome_lbm_trace.log'

# 新文件路径
output_file_path = 'chrome_lbm_check.log'

# 打开原始文件并读取前100行
with open(input_file_path, 'r') as input_file:
    lines = input_file.readlines()  # 读取所有行
    first_100_lines = lines[:100]   # 取前100行

# 将前100行写入新文件
with open(output_file_path, 'w') as output_file:
    output_file.writelines(first_100_lines)