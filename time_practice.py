"""Module providing a function to wait for specific time."""
import time

my_time = int(input('請輸入秒數: '))

# 正著數
# for x in range(my_time):
#     print(x+1)
#     time.sleep(1)

# 倒著數
for x in range(my_time, 0, -1):
    print(x)
    time.sleep(1)

for x in range(my_time, 0, -1):
    # 想要的格式: 02:00
    seconds = x % 60
    minutes = x // 60 % 60
    print(f"{minutes:02}:{seconds:02}")
    time.sleep(1)

print("時間到了")
