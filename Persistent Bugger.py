"""
Name : Persistent Bugger.py
Author  : KhyronLu
Time    : 2021/6/11 12:40 下午
Desc:
"""
def persistence(n):
    # your code here
    if n < 10:
        return 0
    total = 1
    for i in str(n):
        total = total * int(i)

    return 1 + persistence(total)

print(persistence(999))