# Python 的物件導向程式設計 OOP
# 物件(Object)是類別(Class)的實例(Instance)

# 車 => 類別
# 每一台生產出來的車子 => 物件

class Car:
    """Class representing a car"""
    wheels = 4
    def __init__(self, make, model, year, color):
        # 初始化
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    def drive(self):
        """車子啟動"""
        print(self.model + "正在行駛")

    def stop(self):
        """車子停止"""
        print(self.model + "已停止")

car1 = Car("Toyota", "Altis", 2021, "藍色")
car2 = Car("Ford", "Kuga", 2020, "白色")

# print(f"{car1.make} {car1.model} {car1.year} {car1.color}")
# print(f"{car2.make} {car2.model} {car2.year} {car2.color}")

# car1.drive()
# car1.stop()

# car2.drive()

bike = Car("三陽", "勁戰", 2020, "黑色")
bike.wheels = 2

print(f"{car1.model} {car1.wheels}")
print(f"{bike.model} {bike.wheels}")
