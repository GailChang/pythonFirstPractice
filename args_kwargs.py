"""名詞介紹: args, kwargs"""

# args => arguments 任意數量的參數 * => tuple

def add(a, b):
    """加法"""
    return a + b

# print(add(1, 2))

def add2(*args):
    """加法 強化版"""
    total = 0
    for arg in args:
        total += arg
    return total

# print(add2(1,2,3))

# kwargs => 關鍵字 + args (keyword args) ** => dictionary
def print_info(**kwargs):
    """列印 key 及 value"""
    for key, value in kwargs.items():
        print(f"key: {key} value: {value}")

print_info(name="Alice", age="25", occupation="engineer")
