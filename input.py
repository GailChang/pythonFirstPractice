# input 取得使用者輸入

name = input("請輸入名字: ")
print(f"your name is {name}")

# 練習一: 填詞遊戲

adj_1 = input('請輸入 1 個形容詞: ')
noun = input('請輸入名詞: ')
adj_2 = input('請輸入 2 個形容詞: ')
verb = input('請輸入動詞: ')
adj_3 = input('請輸入 3 個形容詞: ')

print(f"今天我去了一個 {adj_1} 的動物園，在展覽中我看到了 {noun} 這個 {noun} 很 {adj_2}，正在 {verb}，我感到很 {adj_3}")

# 練習二: 計算矩形面積

length = float(input('請輸入矩形的長度: '))
width = float(input('請輸入矩形的寬度: '))

area = length * width
print(f"面積為{area} 平方公分")

# 練習三: 購物車程式

item = input('你想購買什麼物品: ')
price = float(input('價格: '))
quantity = int(input('你需要多少件? '))

total = price * quantity
print(f"{quantity} 個 {item} 總價為 ${total}")
