"""
Name : Your order,please.py
Author  : KhyronLu
Time    : 2021/6/11 12:46 下午
Desc:
"""

def you(str1):
    str1 = str1.split()
    print(str1)
    list1 = []
    # str1 = sorted(str1,key)
    for i in range(len(str1)+1):
        for s in str1:
            if str(i) in s:
              list1.append(s)

    list1 = ' '.join(list1)
    print(list1)
    return list1


print(you("is2 Thi1s T4est 3a"))
