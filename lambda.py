"""Python 中的 lambda λ"""

# lambda 有函式的功能 一行就可以寫完

# example 1 - double
def double(x):
    return x * 2

double2 = lambda x : x * 2

# print(double(10))
# print(double2(10))

# example 2
multiply = lambda x, y: x * y
# print(multiply(2, 5))

# example 3 - if else 條件語句
result = lambda x : f"{x}是偶數" if x % 2 == 0 else f"{x}是奇數"
# print(result(10))
# print(result(15))

# example 4 - 處理字串
full_name = lambda first_name, last_name : f"{first_name} {last_name}"
print(full_name("chung", "ling ling"))
