import os

# 文件夹和文件命名
dir_names = [str(i) for i in range(1, 51)]
file_names = ["原著-白话.txt", "简化一.txt", "简化二.txt", "简化三.txt"]

# 创建文件夹和文件
for dir_name in dir_names:
    # 创建文件夹
    os.makedirs(dir_name, exist_ok=True)
    # 在每个文件夹中创建文件
    for file_name in file_names:
        with open(os.path.join(dir_name, file_name), 'w') as f:
            pass  # 创建一个空文件