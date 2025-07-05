"""函式的引數 arguments"""

# 函式的預設引數 (default arguments)
def greet(name, greeting="Hello"):
    """某某 Hello"""
    print(f"{name}, {greeting}")

# greet("John")
# greet("John", "Hi")

# 關鍵字參數 Keyword Arguments
def hello(greeting, title, first_name, last_name):
    """向某人問候"""
    print(f"{greeting}, {title}, {first_name} {last_name}")

# hello("你好", "Mr", "Kate", "Dartson")
# hello(greeting="你好", title="Mr", first_name="Kate", last_name="Dartson")

# 獲得電話號碼
def get_phone(country_code, area_code, first, last):
    """獲得電話號碼"""
    return f"{country_code}-{area_code}-{first}-{last}"

phone = get_phone(country_code="886", area_code="02", first="1234", last="5678")
print(phone)
