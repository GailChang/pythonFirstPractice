"""隨機數練習"""
import random

# randint()
# print( random.randint(1,10) )

# random()
# print( random.random() )

# 列表中隨機選擇一個元素
options = ["剪刀", "石頭", "布"]
rand_option = random.choice(options)
# print(rand_option)

# 將一個列表打亂
cards = ["2", "3", "4", "5", "6", "9", "12"]
random.shuffle(cards)
# print(cards)

# 猜數字遊戲
low = 1
high = 100
number = random.randint(low, high)
guess_count = 0
while True:
    guess = input(f"請從 {low}~{high} 猜一個數字: ")
    guess_number = int(guess)
    guess_count += 1
    if guess_number == number:
        print(f"你猜對了，正確答案是 {number}")
        print(f"你總共猜了 {guess_count} 次")
        break
    elif guess_number < number:
        low = guess_number
        print("你猜的數字小於正確答案")
    else:
        high = guess_number
        print("你猜的數字大於正確答案")
