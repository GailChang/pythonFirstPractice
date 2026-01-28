"""Python 中的 map"""

# map (可迭代的[列表], 函式)

store = [
    ('襯衫', 20), # 美金
    ('褲子', 30),
    ('夾克', 50),
    ('襪子', 10)
]

to_euros = lambda data: (data[0], data[1] * 0.82)
to_twd = lambda data: (data[0], data[1] * 30)

to_usd = lambda data: (data[0], round(data[1] / 30))

# store_euros = list(map(to_euros, store))
# print(store_euros)

store_twd = list(map(to_twd, store))
print(store_twd)

store_usd = list(map(to_usd, store_twd))
print(store_usd)
