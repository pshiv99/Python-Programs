# Rmove duplicate elements recursively

from collections import defaultdict

def removeDuplicate(s):
    flag = True
    for i in range(len(s)-1):
        if s[i+1] == s[i]:
            flag = False
    
    if flag:
        return s
    else:
        res = remDuplicate(s)
        return removeDuplicate(res)


def remDuplicate(s):
    if len(s) == 1:
        return ''
    else:
        for index in range(1, len(s)):
            if s[index] != s[0]:
                break
            
        if index != 1:
            s = remDuplicate(s[index:])
        else:
            s = s[0:index] + remDuplicate(s[index:])
            
        return s

testcases = int(input())

for _ in range(testcases):
    s = input()
    
    s = removeDuplicate(s)
    
    print(s)
            