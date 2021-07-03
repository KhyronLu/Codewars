"""
Name : Highest Scoring Word.py
Author  : KhyronLu
Time    : 2021/6/11 1:12 下午
Desc:
"""
def high(x):
    # Code here

    return max(x.split(), key=lambda k: sum(ord(i)-96 for i in k))


print(high('man i need a taxi up to ubud'))