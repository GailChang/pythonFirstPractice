"""Python 列表推導式(list comprehension)"""

# 列表推導式 => 更少的語法建立新列表

# 第一版寫法
def square(x):
    """平方"""
    return x * x
sample = []
for i in range(1, 11):
    sample.append(square(i))
# print(sample)

# 第二版寫法，使用列表推導式
squares = [
    i * i for i in range(1, 11)
]
print(f"列表推導式 {squares}")

grades = [100, 90, 66, 80, 46, 29, 88]
passed_grades = [g for g in grades if g >= 60]
print(f"通過者: {passed_grades}")
