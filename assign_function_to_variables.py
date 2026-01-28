"""Python 將函式指派給變數"""

def hello():
    """說你好"""
    print("hello")

hi = hello

# 可發現 hello 和 hi 的記憶體位置相同，也就是兩者其實是同一個東西
print(hello)
print(hi)

hi()

say = print
say("oh yeah")
