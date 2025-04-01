def solution(s, n):
    big_alpha = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    small_alpha = list('abcdefghijklmnopqrstuvwxyz')

    result = ''
    for ele in s:
        if ele == ' ':
            result += ' '
        else:
          result += big_alpha[(big_alpha.index(ele) + n) % 26] if ele.isupper() else small_alpha[(small_alpha.index(ele) + n) % 26]
      
    return result