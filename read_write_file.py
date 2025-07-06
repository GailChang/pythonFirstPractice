"""讀取、寫入檔案練習"""

file_path = r"D:\Repo\Workspace\test.txt"
try:
    text = "嗨!\n祝你一切順利"
    # write
    with open(file_path, 'w', encoding="utf-8") as file:
        file.write(text)
    # insert
    with open(file_path, 'a', encoding="utf-8") as file:
        file.write("\n插入文字模式")
    with open(file_path, encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError as e:
    print("找不到檔案")
