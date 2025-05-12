import re
from collections import Counter

def make_multiset(s):
    s = s.upper()
    multiset = []
    
    for i in range(len(s) - 1):
        pair = s[i:i+2]
        if pair.isalpha():
            multiset.append(pair)
    return Counter(multiset)
    
    
def solution(str1, str2):
    multiset1 = make_multiset(str1)
    multiset2 = make_multiset(str2)
    
    inter = sum((multiset1 & multiset2).values())
    union = sum((multiset1 | multiset2).values())
    
    if union == 0:
        return 65536
    return int(inter / union * 65536) 