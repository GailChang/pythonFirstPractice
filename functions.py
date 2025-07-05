"""認識函式/方法(method)"""

def say_hello(number):
    """說你好"""
    print(f"說你好 {number}")

say_hello(1)

# greeting
def greeting(name):
    """greeting"""
    print(f"{name} 你好!")

# add
def add(x, y):
    """加法"""
    return x + y

# substract
def sub(x, y):
    """減法"""
    return x - y

# multiple
def mul(x, y):
    """乘法"""
    return x * y

# devide
def devide(x, y):
    """除法"""
    return x / y

# 將名字轉為大寫
def create_name(first, last):
    """將名字轉為大寫"""
    first = first.capitalize()
    last = last.capitalize()
    return f"{first} {last}"

print(create_name("John", "Witt"))
