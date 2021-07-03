"""
Name : Where my anagrams at?.py
Author  : KhyronLu
Time    : 2021/6/10 11:04 下午
Desc:
"""
def anagrams(word, words):
    #your code here
    list = []
    for w in words:
        flag = 0
        if len(w) == len(word):
            for i in w:
                if i not in word:
                    flag = 1
                if w.count(i) != word.count(i):
                    flag = 1
            if not flag:
                list.append(w)
    print(list)
    return list

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))