"""Python filter 過濾"""

# 可用來過濾可迭代的資料結構(List, ...)

friends = [
    ("Bob", 18),
    ("Steven", 17),
    ("Michael", 19),
    ("Susan", 16)
]

age_filter = lambda data : data[1] >= 18

can_drink_friends = filter(age_filter, friends)
print(list(can_drink_friends))
