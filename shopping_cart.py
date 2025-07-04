# 購物車程式

goods = []
prices = []

# 無窮迴圈
while True:
    good = input('請輸入想購買的物品: (離開請打q)')
    if good.lower() == 'q':
        break
    price = float(input(f"請輸入 {good} 的價格: "))
    goods.append(good)
    prices.append(price)

total = 0
for index, good in enumerate(goods):
    print(f"第 {index + 1} 個商品 | 品名: {good}; 價格: {prices[index]:.2f}")
    total += prices[index]
print(f'總金額: ${total:.2f}')

