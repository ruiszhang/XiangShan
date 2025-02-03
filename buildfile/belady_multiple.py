def process_trace_file(trace_file, array_len, set_count):
    # 初始化set个数组和计数器
    sets = [[None] * array_len for _ in range(set_count)]
    hit = 0
    count = 0
    hit_bool = 0

    # 读取trace文件中的数据
    with open(trace_file, 'r') as file:
        data = file.read().strip().split()

    num = len(data)

    for i in range(num):
        current_address = int(data[i])  # 假设trace文件中的数据是十进制地址
        count += 1

        # 计算set索引和tag
        set_index = (current_address >> 6) & 0x7F  # 第7到第13位（共7位）
        tag = current_address >> 13  # 第13位以上的高位

        # 处理对应的set
        current_set = sets[set_index]

        if tag in current_set:
            # 如果数据已在数组中，hit+1
            hit += 1
            future_occurrences = []
            hit_bool = 1
        else:
            hit_bool = 0
            if None in current_set:
                # 数组中有空位置，插入数据到第一个空位置
                current_set[current_set.index(None)] = tag
                future_occurrences = []
            else:
                # 数组已满，执行替换策略
                future_occurrences = []
                future_tags_in_set = [(int(data[j]) >> 13) for j in range(i + 1, num) if (int(data[j]) >> 6) & 0x7F == set_index]
                for item in current_set:
                    if item in future_tags_in_set:
                        future_occurrences.append(future_tags_in_set.index(item) + i + 1)
                    else:
                        future_occurrences.append(float('inf'))  # 表示不会再出现

                # 找到出现最晚的tag位置进行替换
                replace_index = future_occurrences.index(max(future_occurrences))
                current_set[replace_index] = tag

        print(f"Step {count}: Address={data[i]}, Set={set_index}, Tag={tag}, Sets={current_set}, Hit={hit_bool}, reuse_dist={future_occurrences}")

    print(f"Total hits: {hit}")
    print(f"Total counts: {count}")
    print(f"Hit Rate: {hit/count}")

# 调用函数
trace_file = '/nfs/home/zhangruisi/myXiangShan10/xs-env/buildfile/chrome_tltest_trace.txt'  # 替换为你的trace文件路径
array_len = 8  # 替换为数组的长度
set_count = 128  # 假设set数目是128
process_trace_file(trace_file, array_len, set_count)