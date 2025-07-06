"""例外處理(Error handling, 異常處理)"""

# exception

try:
    x = int(input("請輸入一個整數: "))
    y = int(input("請輸入另一個整數: "))

    print(x / y)
# except ValueError:
#     print("請輸入整數")
# except ZeroDivisionError:
#     print("除數不能為零")
except (ValueError, ZeroDivisionError):
    print("出現錯誤，請重新輸入")
else:
    print("else")
# finally:
#     print("程式執行結束")
