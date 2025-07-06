"""作用域"""

# 變數範圍與作用域
# LEGB 作用域順序

# L - Local 區域
# E - enclosed
# G - Global 全域
# B - built-in 內建

# 變數範圍

def function_one():
    a = 1
    print(a)
    def function_two():
        b = 2
        print(a)
        print(b)
    function_two()

# function_one()

from math import e
print(e)
print(round(e))
