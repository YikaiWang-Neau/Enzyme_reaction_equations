# 读取文件并去除所有重复行，只保留第一次出现的
def remove_all_duplicates(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # 用于记录已出现的行
    seen_lines = set()
    unique_lines = []
    
    for line in lines:
        if line not in seen_lines:
            unique_lines.append(line)
            seen_lines.add(line)

    # 写回去除重复后的内容
    with open(file_path, 'w') as file:
        file.writelines(unique_lines)

# 调用函数
remove_all_duplicates('numbers.txt')
