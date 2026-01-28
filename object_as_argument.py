"""Python 物件當成引數"""

class Car:
    """車子"""
    color = None

def change_color(car, color):
    """修改車子顏色"""
    car.color = color

car1, car2, car3 = Car(), Car(), Car()

print(f"{car1.color}, {car2.color}, {car3.color}")

change_color(car1, "紅色")
change_color(car2, "藍色")
change_color(car3, "黑色")

print(f"{car1.color}, {car2.color}, {car3.color}")
