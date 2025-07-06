"""進行檔案偵測"""

import os

# str = "D:\\Repo\\Workspace\\"
str2 = r"D:\Repo\Workspace\test.txt"
print(str2)

if os.path.exists(str2):
    print("路徑存在")
    if os.path.isfile(str2):
        print("該路徑為檔案")
    elif os.path.isdir(str2):
        print("該路徑為目錄")
    else:
        print("other")
else:
    print("路徑不存在")
