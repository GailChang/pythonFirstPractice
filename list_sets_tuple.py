"""Module providing the basic concept of list, set, and tuple."""

# ==================
#        list
# ==================

# 可以重複，且有順序
# list 是一個有序的集合，可以包含重複的元素
fruits = ['apple', 'orange', 'banana', 'coconut']
# print(fruits[0])
# print(fruits[0:-1])

fruits.append('guava')
fruits.remove('coconut')

# for f in fruits:
    # print(f)

# print(fruits.index('banana'))

fruits.append('apple')
fruits.append('apple')
# print(fruits.count('apple'))

fruits.reverse()
# print(fruits)

# ==================
#        set
# ==================

# 不能重複，且無順序

good_set = {'🍎', '🍊', '🍌', 'banana', 'coconut'}
good_set.add('coconut')  # 重複的元素不會被添加

# 即使輸入重複的，也會被忽略掉
for s in good_set:
    print(s, end=" ")

good_set.add('watermelon')
if 'watermelon' in good_set:
    print('it exists')

good_set.remove('banana')  # 移除元素
print(good_set)

# ==================
#     tuple 元組
# ==================

many_tuple = ('apple', 'orange', 'banana', 'apple')
print(many_tuple.count('apple'))
print(many_tuple.index('orange'))

# 不能在宣告後增刪
# many_tuple.add('apple')
