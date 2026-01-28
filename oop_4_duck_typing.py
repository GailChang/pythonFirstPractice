"""Duck Typing"""

class Duck:
    """鴨子"""
    def walk(self):
        print("鴨子在走路")
    def talk(self):
        print("鴨子在呱呱呱")

class Chicken:
    """雞"""
    def walk(self):
        print("雞在走路")
    def talk(self):
        print("雞在咕咕叫")

# 即使沒有繼承的關係，也可以當作同一類型的類別使用
class Person:
    """人"""
    def catch(self, duck):
        duck.walk()
        duck.talk()

person, duck, chicken = Person(), Duck(), Chicken()

person.catch(duck)
person.catch(chicken)
