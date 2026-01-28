"""Python 獠牙運算符"""

# 獠牙運算符 :
# 賦值表達式 :=
# 賦值運算子 =

# Python 3.8

happy = True

# print(happy)
# print(happy := False)

# 錯誤寫法，使用 = 的時候不會迴傳值
# print(happy = True)

foods = []

# 第一版寫法
# while True:
#     food = input("你喜歡什麼食物?")
#     if food == 'quit':
#         break
#     foods.append(food)

# 第二版寫法，使用獠牙運算符
# while food := input("你喜歡什麼食物?"):
#     if food == 'quit':
#         break
#     foods.append(food)

# 第三版寫法，進一步簡化
while (food := input("你喜歡什麼食物?")) != 'quit':
    foods.append(food)

print(foods)
