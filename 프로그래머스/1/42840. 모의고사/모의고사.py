def solution(answers):
    result = []
    score = [0, 0, 0]
    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for idx, answer in enumerate(answers):
        if answer == person1[idx % len(person1)]:
            score[0] += 1
        if answer == person2[idx % len(person2)]:
            score[1] += 1
        if answer == person3[idx % len(person3)]:
            score[2] += 1
    
    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result