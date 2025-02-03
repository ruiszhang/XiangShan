# def count_specific_rows(log_file):
#     count_last_third_is_1 = 0
#     count_both_conditions = 0

#     with open(log_file, 'r') as file:
#         for line in file:
#             columns = line.strip().split('|')
#             if len(columns) >= 3:  # Ensure there are enough columns
#                 # Check if the third-to-last column is '1'
#                 if columns[-3] == '1':
#                     count_last_third_is_1 += 1

#                     # Additionally check if the eleventh-to-last column is '1'
#                     if len(columns) >= 11 and columns[-11] == '1':
#                         count_both_conditions += 1

#     return count_last_third_is_1, count_both_conditions

# # 使用方法
# log_file = '/nfs/home/zhangruisi/myXiangShan10/tl-test/build/chrome_1.log'  # 替换为你的.log文件路径
# last_third_count, both_conditions_count = count_specific_rows(log_file)
# print(f"倒数第三列为1的行数: {last_third_count}")
# print(f"倒数第三列为1且倒数第十一列为1的行数: {both_conditions_count}")




# def count_specific_rows(log_file):
#     count_last_third_is_1 = 0
#     count_both_conditions = 0

#     # First pass to count total lines
#     with open(log_file, 'r') as file:
#         total_lines = sum(1 for _ in file)
    
#     half_index = total_lines // 2

#     # Second pass to process only the second half of the lines
#     with open(log_file, 'r') as file:
#         for i, line in enumerate(file):
#             if i >= half_index:
#                 columns = line.strip().split('|')
#                 if len(columns) >= 3:  # Ensure there are at least 3 columns
#                     # Check if the third-to-last column is '1'
#                     if columns[-3] == '1':
#                         count_last_third_is_1 += 1

#                         # Additionally check if the eleventh-to-last column is '1'
#                         if len(columns) >= 11 and columns[-11] == '1':
#                             count_both_conditions += 1

#     return count_last_third_is_1, count_both_conditions

# # Usage
# log_file = '/nfs/home/zhangruisi/myXiangShan10/tl-test/build/chrome_1.log'  # Replace with your .log file path
# last_third_count, both_conditions_count = count_specific_rows(log_file)
# print(f"Count of rows with the third-to-last column as 1: {last_third_count}")
# print(f"Count of rows with both the third-to-last and eleventh-to-last columns as 1: {both_conditions_count}")



def count_specific_rows(log_file):
    count_last_third_is_1 = 0
    count_both_conditions = 0

    with open(log_file, 'r') as file:
        for line in file:
            columns = line.strip().split('|')
            if len(columns) >= 3:  # Ensure there are at least 3 columns
                # Check if the third-to-last column is '1'
                if columns[-3] == '1':
                    count_last_third_is_1 += 1

                    # Additionally check if the eleventh-to-last column is '1'
                    if len(columns) >= 11 and columns[-11] == '1':
                        count_both_conditions += 1

    return count_last_third_is_1, count_both_conditions

# Usage
log_file = '/nfs/home/zhangruisi/myXiangShan10/tl-test/build/chrome_1.log'  # Replace with your .log file path
last_third_count, both_conditions_count = count_specific_rows(log_file)
print(f"Count of rows with the third-to-last column as 1: {last_third_count}")
print(f"Count of rows with both the third-to-last and eleventh-to-last columns as 1: {both_conditions_count}")
