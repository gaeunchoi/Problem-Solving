import re
from collections import Counter
def solution(s):
    numbers = re.findall(r'\d+', s)
    
    count = Counter(numbers)
    sorted_nums = sorted(count.items(), key = lambda x: -x[1])
    
    return [int(num) for num, _ in sorted_nums]
    