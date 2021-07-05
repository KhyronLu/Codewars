"""
Name : Break camelCase.py
Author  : KhyronLu
Time    : 2021/7/4 11:29 下午
Desc:
"""
def solution(s):
    str = ""
    for i in s:
        if i.isupper():
            i = ' '+i
        else:i
        str += "".join(i)
    print(str)
    return str

#可以简写为
def solution_new(s):
    return "".join(" " + i if i.isupper() else i for i in s)
print(solution_new("wwwSdwu"))