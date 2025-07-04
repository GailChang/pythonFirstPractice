fruits = ['apple', 'orange', 'banana', 'coconut']
print(fruits[0])
print(fruits[0:-1])

fruits.append('guava')
fruits.remove('coconut')

for f in fruits:
    print(f)

print(fruits.index('banana'))

fruits.append('apple')
fruits.append('apple')
print(fruits.count('apple'))

fruits.reverse()
print(fruits)

# ==================
#        set
# ==================

# 不能重複，且無順序

good_set = {'apple', 'orange', 'banana', 'banana', 'coconut'}

# 即使輸入重複的，也會被忽略掉
for s in good_set:
    print(s, end=" ")

good_set.add('watermelon')
if 'apple' in good_set:
    print('it exists')

# ==================
#     tuple 元組
# ==================

many_tuple = ('apple', 'orange', 'banana', 'apple')
print(many_tuple.count('apple'))
print(many_tuple.index('orange'))

# 不能在宣告後增刪
many_tuple.add('apple')
