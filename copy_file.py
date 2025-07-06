"""複製檔案練習"""

import shutil
import os

source_root = r"D:\Repo\Workspace"
source_file = f"{source_root}\\source_file.txt"
output_file = f"{source_root}\\output_file.txt"

if os.path.exists(output_file):
    os.remove(output_file)

# copyfile
# 複製內容，不複製原數據(metadata)。只能複製檔案
# shutil.copyfile(source_file, output_file)

# copy
# 複製內容，也複製原數據(metadata，包含權限)。只能複製檔案
# shutil.copy(source_file, output_file)

# copy2
# 複製內容，也複製原數據(metadata + 時間戳 + 權限)。只能複製檔案
shutil.copy2(source_file, output_file)

# copytree
# 複製內容，也複製原數據(metadata + 時間戳 + 權限)。可以複製資料夾
source_dir = f"{source_root}\\sourceDir"
output_dir = f"{source_root}\\outputDir"

# 請確保 output_dir 不存在：
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)  # 先刪除舊的 output_dir

shutil.copytree(source_dir, output_dir)
