def solution(lottos, win_nums):
    current_nums = [n for n in lottos if n in win_nums]
    zero_cnt = lottos.count(0)
    
    min_match = len(current_nums)
    max_match = min_match + zero_cnt
    
    def get_rank(cnt):
        return 7 - cnt if cnt >= 2 else 6
    
    return [get_rank(max_match), get_rank(min_match)]