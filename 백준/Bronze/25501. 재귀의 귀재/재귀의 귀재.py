import sys

T = int(input())

def recursion(s, l, r):
    global cnt
    cnt += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

for _ in range(T):
    cnt = 0
    S = list(map(str, input().rstrip()))
    print(isPalindrome(S), cnt)