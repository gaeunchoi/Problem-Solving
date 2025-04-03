def solution(cards1, cards2, goal):
    result = []
    idx1 = idx2 = 0
    
    for i in range(len(goal)):
        if idx1 < len(cards1) and goal[i] == cards1[idx1]:
            result.append(goal[i])
            idx1 += 1
        elif idx2 < len(cards2) and goal[i] == cards2[idx2]:
            result.append(goal[i])
            idx2 += 1
        else:
            break

    return "Yes" if goal == result else "No"