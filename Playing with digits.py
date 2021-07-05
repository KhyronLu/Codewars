"""
Name : Playing with digits.py
Author  : KhyronLu
Time    : 2021/7/5 2:48 下午
Desc:
"""

def dig_pow(n, p):
    # your code
    c = list(str(n))
    print(c)
    sum = 0
    for i in c:
        sum += int(i)**p
        p = p+1
    print(sum)
    if sum % n == 0:
        print(sum // n)
        return sum // n
    else:
        return -1

print(dig_pow(46288, 3))