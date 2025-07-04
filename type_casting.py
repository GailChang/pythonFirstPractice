# 型別轉換 type casting

name = 'John'
age = 25
gpa = 1.9
student = True

# 顯示型別轉換

# print(type(name))
# print(type(age))
# print(type(gpa))
# print(type(student))

age = float(age)
print(age)
print(type(age))

gpa = int(gpa)
print(gpa)
print(type(gpa))

student = str(student)
print(student)
print(type(student))

# 隱式型別轉換

x = 10
y = 2.0
x = x/y

print(x)
print(type(x))

