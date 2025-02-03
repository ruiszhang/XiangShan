def process_log_file(input_file, output_file):
    # 指定要删除的列（1-based index），然后转换为0-based index
    columns_to_delete = {2, 5, 6, 7, 8, 10, 11, 16}
    columns_to_delete = {i - 1 for i in columns_to_delete}

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            data = line.strip().split('|')

            # Convert columns 4 and 3 (index 3 and 2) to binary and pad with zeros
            binary_col4 = format(int(data[3]), 'b').zfill(64)  # Assuming 32-bit integers(user1)
            binary_col3 = format(int(data[2]), 'b').zfill(64)  # Assuming 32-bit integers(user0)

            # Combine the binary strings
            combined_binary = binary_col4 + binary_col3

            # Ensure the combined binary string is of sufficient length
            combined_binary = combined_binary.zfill(128)

            # Extract the 1st to 4th bits (0-indexed positions 0 to 3)
            first_segment = binary_col3[59:63]
            first_segment_decimal = int(first_segment, 2)

            # Extract the 38th to 76th bits (0-indexed positions 37 to 75)
            # second_segment = combined_binary[51:90]   # 39-bit
            second_segment = combined_binary[77:90]     # 13-bit
            second_segment_decimal = int(second_segment, 2)

            # Remove specified columns including original columns 3 and 4
            filtered_data = [
                data[i] for i in range(len(data)) if i not in columns_to_delete and i != 2 and i != 3
            ]

            # Insert the extracted values at the correct positions
            filtered_data.insert(1, str(first_segment_decimal))  # New 2nd column(reqsource)
            filtered_data.insert(2, str(second_segment_decimal)) # New 3rd column(pc)
            # filtered_data.insert(3, str(combined_binary)) # New 3rd column(user)

            # Reorder the columns as specified
            reordered_data = [
                filtered_data[0], 
                filtered_data[-1],  # Last column becomes the 2nd column
                '0',               # Add a zero as the new 3rd column
                filtered_data[-2],  # Second last column becomes the 4th column
                filtered_data[-3],  # Third last column becomes the 5th column
                filtered_data[3],   # 4th column becomes the 6th column
                filtered_data[4],   # 5th column becomes the 7th column
                filtered_data[1],   # 2nd column becomes the second last column
                filtered_data[2]    # 3rd column becomes the last column
            ]

            if reordered_data[3] == '0':
                reordered_data[3] = '1'
            elif reordered_data[3] == '2':
                reordered_data[3] = '4'


            # Write the processed data to the output file
            outfile.write(','.join(reordered_data) + '\n')

# 使用方法
input_log_file = 'chrome_mcf.log'  # 输入文件路径
output_log_file = 'chrome_mcf_trace.log'  # 输出文件路径
process_log_file(input_log_file, output_log_file)