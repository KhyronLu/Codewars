"""
Name : Which are in?.py
Author  : KhyronLu
Time    : 2021/6/11 12:25 下午
Desc:
"""
import plistlib


def in_array(array1, array2):
    # your code
    t = []
    for i in array1:
        for j in array2:
            if i in j:
                t.append(i)
    print(t)
    # t = set(t)
    # t = list(t)
    t = sorted(set(t))
    print(t)
    return t

print(in_array(["tarp", "mice", "bull"],["lively", "alive", "htarp", "sharp", "armstrong"]))