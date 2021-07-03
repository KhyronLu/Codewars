"""
Name : TheHashtagGenerator.py
Author  : KhyronLu
Time    : 2021/6/12 1:25 下午
Desc:
"""

def generate_hashtag(s):
    #your code here
    if not s or len(s)>140:
        return False
    else:
        s = s.title()
        s = s.split()
        s.insert(0,"#")
        s = ''.join(s)
        print(s)
        return s


print(generate_hashtag('Do We have A Hashtag'))