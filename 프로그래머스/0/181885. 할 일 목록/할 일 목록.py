def solution(todo_list, finished):
    answer = []
    for tf in range(len(finished)):
        if not finished[tf]:
            answer.append(todo_list[tf])        
    return answer