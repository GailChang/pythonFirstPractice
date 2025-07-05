"""點餐系統練習"""

menu = {
    "披薩": 300,
    "爆米花": 150,
    "可樂": 50,
    "薯條": 100,
    "雞塊": 200,
}

print("歡迎使用點餐系統！\n"
"以下是我們的菜單：")
for index, (item, price) in enumerate(menu.items()):
    print(f"項目{index+1}: {item}: {price}元")

cart = []
TOTAL = 0

while True:
    food = input("請輸入您想點的食物名稱（輸入q結束）：")
    if food.lower() == 'q':
        break
    elif menu.get(food) is None:
        print("沒有這個商品")
    else:
        cart.append(food)
        TOTAL += menu.get(food)
        print(food, end=" ")

print(f"總共: {TOTAL}元")
