"""Python Zip 函式"""

usernames = ["Bob", "Steven", "Sam"]
passwords = ("123", "321", "555")
bdays = ['1998-02-05', '1994-04-22', '1986-11-17']

users = zip(usernames, passwords, bdays)
for i in users:
    print(i)
print(list(users))

user_dict = dict(users)
print(user_dict)
