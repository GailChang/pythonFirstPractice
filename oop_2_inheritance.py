"""OOP - Python 的繼承"""
# 父類別 <-> 子類別

class Animal:
    """動物"""
    aLive = True

    def eat(self):
        """吃東西"""
        print("這個動物正在吃東西")
    def sleep(self):
        """睡覺"""
        print("這個動物正在睡覺")

class Rabbit(Animal):
    """兔子"""
    def junp(self):
        """跳"""
        print("這隻兔子正在跳")

# animal = Animal()
# animal.eat()
# animal.sleep()

# rabbit = Rabbit()
# rabbit.eat()
# rabbit.sleep()
# rabbit.junp()

class Mammel(Animal):
    """哺乳類"""
    def hi(self):
        """嗨"""
        print("我是哺乳類")

# 覆寫繼承來的方法
class Cat(Mammel):
    """貓"""
    def eat(self):
        print("小貓在吃魚")

class Dog(Mammel):
    """狗"""
    def eat(self):
        print("小狗正在啃骨頭")

mammel, cat, dog = Mammel(), Cat(), Dog()

mammel.eat()
cat.eat()
dog.eat()

class Fish(Animal):
    """魚"""
    def swim(self):
        """游泳"""
        print("魚正在游泳")

class Hawk(Animal):
    """老鷹"""
    def fly(self):
        """飛"""
        print("老鷹正在飛")

# fish = Fish()
# fish.swim()
# fish.eat()
# fish.sleep()

# hawk = Hawk()
# hawk.fly()
# hawk.eat()
# hawk.sleep()
