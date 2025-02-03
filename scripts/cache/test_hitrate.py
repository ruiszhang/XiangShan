import os
import sys

args = sys.argv
mode = args[1]

if(mode == '1'):
    # 搜索的文件名
    target_file = "simulator_err.txt"

    # 输出文件名
    output_file = "hitrate1.txt"

    # 搜索的特定内容
    # specific_content_A = "selfdir_A_hit"
    # specific_content_B = "selfdir_A_req"
    # specific_content_C = "l3cacheOpt.topDown: E2_L3AReqSource_"
    # specific_content_C = "a_req_miss,"
    # specific_content_D = "a_req_hit,"
    specific_content_C = "acquire_miss,"
    specific_content_D = "acquire_hit,"
    # # specific_content_C = "selfdir_C_hit"
    # # specific_content_D = "selfdir_C_req"
    # specific_content_E = "selfdir_hit"
    # specific_content_F = "selfdir_req"

    # 遍历目录
    for root, dirs, files in os.walk("."):
        # 遍历每个文件
        for file in files:
            # 检查文件名是否匹配目标文件
            if file == target_file:
                # 构建文件路径
                file_path = os.path.join(root, file)

                # 读取特定内容并写入输出文件
                with open(file_path, 'r') as input_file:
                    lines = input_file.read().splitlines()
                    for line in lines:
                        if specific_content_C in line or specific_content_D in line:
                            # 写入输出文件，包含文件夹名和特定内容所在行
                            with open(output_file, 'a') as output:
                                output.write(f"Folder: {root}\n")
                                output.write(line)
                                output.write("\n")

##############################################################################################

elif(mode == '2'):
    input_file = 'hitrate1.txt'  # 输入文件
    output_file = 'hitrate2.txt'  # 输出文件
    lines_to_keep = 16  # 每隔lines_to_keep行保留的行数

    with open(input_file, 'r') as file:
        lines = file.readlines()

    with open(output_file, 'w') as file:
        for i in range(len(lines)):
            if i % (lines_to_keep * 2) >= lines_to_keep:
                file.write(lines[i])

else:
    print("Wrong mode! 1 for first step and 2 for second step!")
