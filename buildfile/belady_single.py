def process_trace_file(trace_file, array_len):
    # 初始化数组和计数器
    tags = [None] * array_len
    hit = 0
    count = 0
    hit_bool = 0

    # 读取trace文件中的数据
    with open(trace_file, 'r') as file:
        data = file.read().strip().split()

    num = len(data)

    for i in range(num):
        current_data = data[i]
        count += 1

        if current_data in tags:
            # 如果数据已在数组中，hit+1
            hit += 1
            hit_bool = 1
            future_occurrences = []
        else:
            hit_bool = 0
            if None in tags:
                # 数组中有空位置，插入数据到第一个空位置
                tags[tags.index(None)] = current_data
                future_occurrences = []
            else:
                # 数组已满，执行替换策略
                future_occurrences = []
                for tag in tags:
                    if tag in data[i+1:]:
                        future_occurrences.append(data[i+1:].index(tag) + i + 1)
                    else:
                        future_occurrences.append(float('inf'))  # 表示不会再出现
                
                # 找到出现最晚的tag位置进行替换
                replace_index = future_occurrences.index(max(future_occurrences))
                tags[replace_index] = current_data

        print(f"Step {count}: Data={current_data}, Tags={tags}, Hit={hit_bool}, reuse_dist={future_occurrences}")

    print(f"Total hits: {hit}")
    print(f"Total counts: {count}")

# 调用函数
trace_file = '/nfs/home/zhangruisi/myXiangShan10/xs-env/buildfile/chrome_tltest_trace.txt'  # 替换为你的trace文件路径
array_len = 4  # 替换为数组的长度
process_trace_file(trace_file, array_len)