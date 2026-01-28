"""super 方法"""

class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        super().__init__()
        print("B")

class C(A):
    def __init__(self):
        super().__init__()
        print("C")

class D(B, C):
    def __init__(self):
        super().__init__()
        print("D")

# d = D()
# print(D.__mro__)

class Rectangle:
    """矩形"""
    def __init__(self, length, width):
        self.length = length
        self.width = width
        print("矩形的初始化已執行")

class Square(Rectangle):
    """正方形"""
    def __init__(self, length, width):
        super().__init__(length, width)
        print("正方形的初始化已執行")

# 長寬高
class Cube(Rectangle):
    """立方體"""
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height
        print(f"立方體的長寬高是{length}, {width}, {height}")

cube = Cube(10, 20, 30)
