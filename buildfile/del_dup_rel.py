def remove_specific_duplicates(input_file, temp_file, output_file):
    from collections import defaultdict
    import os

    # Step 1: Identify rows to be removed
    row_map = defaultdict(list)
    rows_to_remove = set()

    # Read file and categorize rows
    with open(input_file, 'r') as infile:
        for line in infile:
            data = line.strip().split(',')
            if len(data) > 5:
                key = (data[3], data[4], data[5])  # (4th, 5th, 6th columns)
                row_map[key].append(data)
    
    # Determine rows to remove based on the 2nd column difference
    for key, group in row_map.items():
        if len(group) > 1:
            # Sort by the 2nd column to easily check for difference of 1
            sorted_group = sorted(group, key=lambda x: int(x[1]))
            for i in range(len(sorted_group) - 1):
                if int(sorted_group[i + 1][1]) - int(sorted_group[i][1]) == 1:
                    # Mark the second row for removal
                    rows_to_remove.add(tuple(sorted_group[i + 1]))

    # Step 2: Write filtered lines to a temporary file, removing the first column
    with open(input_file, 'r') as infile, open(temp_file, 'w') as tempfile:
        for line in infile:
            data = line.strip().split(',')
            if len(data) > 5 and tuple(data) not in rows_to_remove:
                # Remove the first column and write the line
                filtered_data = data[1:]  # Remove the first column
                filtered_data[0] = str(int(filtered_data[0]) + 10000)
                tempfile.write(','.join(filtered_data) + '\n')

    # Step 3: Rename the temporary file to the output file
    os.rename(temp_file, output_file)

# 使用方法
input_log_file = 'chrome_mcf_trace.log'  # 输入文件路径
temp_file = 'temp_filtered.log'  # 临时文件路径
output_log_file = 'chrome_mcf_final.txt'  # 输出文件路径
remove_specific_duplicates(input_log_file, temp_file, output_log_file)