"""Python 字典入門"""

# 字典是 Python 中的一種資料結構，用於存儲鍵值對（key-value pairs）。
# 字典的鍵必須是唯一的，並且可以是不可變類型（如字符串、數字或元組）。
# 字典的值可以是任何類型，包括列表、元組、字典等。
# 字典的基本語法如下：
capital = {
    "United States": "Washington, D.C.",
    "Canada": "Ottawa",
    "Mexico": "Mexico City",
    "Japan": "Tokyo",
    "Taiwan": "Taipei",
}

# get() 方法用於從字典中獲取指定鍵的值，如果鍵不存在，則返回 None 或指定的默認值。
# print(capital.get("United States"))  # 輸出: Washington, D.C.

# update() 方法用於更新字典中的鍵值對，如果鍵不存在，則添加新的鍵值對。
capital.update({"Taiwan": "Kaohsiung"})
capital.update({"Thailand": "Bangkok"})
# print(capital)

# pop() 方法用於刪除字典中指定鍵的鍵值對，並返回該鍵的值。
capital.pop("UK") # 如果鍵不存在，則會引發 KeyError
capital.pop("UK", "Key not found") # 如果鍵不存在，則返回指定的默認值。此時不會引發 KeyError
capital.pop("Japan")
# print(capital)

# values() 方法用於獲取字典中所有值的列表。
print(capital.values())

# keys() 方法用於獲取字典中所有鍵的列表。
print(capital.keys())

# items() 方法用於獲取字典中所有鍵值對的列表。
print(capital.items())
