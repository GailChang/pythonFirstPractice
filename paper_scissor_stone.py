"""猜拳遊戲"""
import random

options = ["paper", "scissor", "stone"]
pc_choice = random.choice(options)
while True:
    player_choice = input("請玩家選擇你要出什麼: ")
    if player_choice in options:
        if player_choice == pc_choice:
            pc_choice = random.choice(options)
            print("平局，請再出一次")
        else:
            break
    print("請出 paper, scissor, stone 任一個")

player_win = False
if options.index(player_choice) == 0 or options.index(pc_choice) == 0:
    player_win = options.index(player_choice) == 0
elif options.index(player_choice) > options.index(pc_choice):
    player_win = True

print(f"玩家出:{player_choice} 電腦出: {pc_choice}")
if player_win:
    print("玩家獲勝")
else:
    print("玩家落敗XDDDDD")
