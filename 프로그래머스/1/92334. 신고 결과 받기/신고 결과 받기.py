def solution(id_list, report, k):
    answer = {key: [] for key in id_list}
    result = {key: 0 for key in id_list}
    for info in report:
        userId, targetId = info.split(" ")
        if userId not in answer[targetId]:
            answer[targetId].append(userId)
    
    for userId in answer:
        if len(answer[userId]) >= k:
            for user in answer[userId]:
                result[user] += 1
    return list(result.values())