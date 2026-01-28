"""Python 中的 time"""

# 系統初始時間
import time
# print(time.ctime(0))
# print(time.time())

# 格式化時間
local_time = time.localtime()
print(f"格式化的時間: {time.strftime("%Y-%m-%d %H:%M:%S", local_time)}")

time_string = "2021-01-31 12:12:12"
time_object = time.strptime(time_string, "%Y-%m-%d %H:%M:%S")
print(time_object)
