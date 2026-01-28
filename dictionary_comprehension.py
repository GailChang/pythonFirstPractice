"""Python 字典推導式"""

# dictionary = {key: <expression> for key, value in iterable}

# example 1 - 華氏轉攝氏運算
cities_in_f = {'LA': 120, 'New Yorks': 65, 'Chicago': 50, 'Miami': 150}
cities_in_c = { key: round((value - 32) * 5/9, 2) for key, value in cities_in_f.items()}

print(cities_in_f)
print(cities_in_c)

# example 2 - 條件判斷
weather = {'台北': '大晴天', '台中': '大晴天', '宜蘭': '下雨', '台東': '下雨'}

sunny_weather = { key: value for key, value in weather.items() if value == '大晴天'}
print(sunny_weather)

# example 3 - 條件判斷 + 函式
def check_temperature(value):
    """決定體感溫度"""
    if value >= 70:
        return '熱'
    elif value >= 40:
        return '溫暖'
    else:
        return '冷'
description_cities = { key: check_temperature(value) for key, value in cities_in_f.items()}
print(description_cities)
