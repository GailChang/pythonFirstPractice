"""骰子遊戲練習"""

# 骰出骰子之後，顯示總和圖案
# 使用 Unicode 字元來製作骰子的圖案

import random

dice_art = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"
    ),
    2: (
        "┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘"
    ),
    3: (
        "┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"
    ),
    4: (
        "┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"
    ),
    5: (
        "┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"
    ),
    6: (
        "┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘"
    )
}

def output_dice_image(number):
    """print the dice art with specific number"""
    for pi in range(5):
        print(dice_art.get(number)[pi])

num_dice = int(input("請輸入要擲幾個骰子: "))
dice = []
for i in range(num_dice):
    this_number = random.randint(1, 6)
    dice.append(this_number)

# 輸出結果
for d in dice:
    output_dice_image(d)

print(f"總共 {sum(dice)}")
