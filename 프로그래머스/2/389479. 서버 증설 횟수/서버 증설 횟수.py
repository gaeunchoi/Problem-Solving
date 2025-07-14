def solution(players, m, k):
    result = 0
    servers = [0 for _ in range(24)]
    
    for idx, player in enumerate(players):
        if player // m > servers[idx]:
            add_server_cnt = player // m - servers[idx]
            
            for i in range(k):
                if idx + i < 24:
	                servers[idx+i] += add_server_cnt
            
            result += add_server_cnt
    
    return result