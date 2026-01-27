"""Python 中的方法鏈 Method Chaining"""

# car.turn_on().drive().brake().turn_off()

class Car:
    """車"""
    def turn_on(self):
        """啟動引擎"""
        print("你啟動了引擎")
        return self
    def drive(self):
        """開車"""
        print("你開車了")
        return self
    def brake(self):
        """煞車"""
        print("你踩了煞車")
        return self
    def turn_off(self):
        """關閉引擎"""
        print("你關閉了引擎")
        return self

car = Car()
car.turn_on().drive().brake().turn_off()
