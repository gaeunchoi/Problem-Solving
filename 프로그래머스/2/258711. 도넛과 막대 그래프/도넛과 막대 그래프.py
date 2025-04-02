def edges_cnt(edges):
    # cnt_edges 딕셔너리 생성 
    # 딕셔너리에는 해당 노드에 나가고 들어오는 에지 수를 저장        
    cnt_edges = {}
    for a, b in edges:
        if not cnt_edges.get(a):
            cnt_edges[a] = [0, 0]
        if not cnt_edges.get(b):
            cnt_edges[b] = [0, 0]

        cnt_edges[a][0] += 1
        cnt_edges[b][1] += 1           

    return cnt_edges 

def solution(edges):
    answer = [0, 0, 0, 0]
    num_edges = edges_cnt(edges)

    for num_node, edges in num_edges.items():
        # 생성 정점은 나가는게 2개 이상, 들어오는게 없다
        if edges[0] >= 2 and edges[1] == 0:
            answer[0] = num_node
        # 막대그래프는 나가는게 0개, 들어오는게 1개(이상이어도 되나)
        elif edges[0] == 0 and edges[1] >= 1:
            answer[2] += 1
        # 8자 그래프는 나가는게 2개 이상, 들어오는게 2개 이상
        elif edges[0] >= 2 and edges[1] >= 2:
            answer[3] += 1

    # 도넛은 생성 정점의 나가는 엣지 수에서 막대 그래프 개수, 8자 그래프 개수 빼기
    answer[1] = num_edges[answer[0]][0] - answer[2] - answer[3]            

    return answer