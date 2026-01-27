import os
import shutil
import send2trash

path = r"D:\Repo\Workspace"

# 刪除檔案
# os.remove(f"{path}/test.txt")

# 刪除空資料夾
# os.rmdir(f"{path}/newFolder")

# 刪除資料夾及其內容
# shutil.rmtree(f"{path}/newFolder")

# 丟到資源回收桶
send2trash.send2trash(fr"{path}\test.txt")
