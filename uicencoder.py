import os

if __name__ == '__main__':
    os.system('powershell -Command "pyside6-uic -o main_window.py MainWindow.ui"')


    # os.system('powershell -Command "pyside6-uic MainWindow.ui > mainWindow.py"')

    #
    # # 从 UTF-16 文件读取并转换为 UTF-8
    # with open('mainWindow.py', 'r', encoding='utf-16') as infile:
    #     content = infile.read()  # 读取文件内容
    #
    # with open('mainWindow.py', 'w', encoding='utf-8') as outfile:
    #     outfile.write(content)  # 将内容写入 UTF-8 文件


    with open('main_window.py', 'r', encoding='utf-8') as f:
        content = f.read()  # 读取文件内容

    # 转换 Unicode 编码为原始字符
    decoded_content = content.encode('utf-8').decode('unicode_escape')

    # 将解码后的内容写入新文件
    with open('main_window.py', 'w', encoding='utf-8') as f:
        f.write(decoded_content)
