# -*- coding: utf-8 -*-
import webbrowser

# 文件路径
file_path = 'urls.txt'

# 逐行读取文件并打开网址
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        url = line.strip()
        if url:  # 确保不处理空行
            webbrowser.open(url)
