def convertTime(t):
    h, m = divmod(t, 100)
    return 60 * h + m

def solution(schedules, timelogs, startday):
    answer = 0
    for i in range(len(schedules)):
        day = startday - 1
        targetTime = convertTime(schedules[i])

        # timelogs[i]를 정렬하여 가장 빠른 출근 시간부터 확인
        for time in timelogs[i]:
            # 주말 만나면 넘기기
            if day in [5, 6]:
                day = (day+1)%7
                continue

            t = convertTime(time)

            # 지각 체크
            if t > targetTime + 10:
                break
            else:
                day += 1 

        else:
            answer += 1

    return answer

print(solution([700, 800, 1100],	[[710, 2359, 1050, 700, 650, 631, 659], [800, 801, 805, 800, 759, 810, 809], [1105, 1001, 1002, 600, 1059, 1001, 1100]],	5))
print(solution([730, 855, 700, 720],	[[710, 700, 650, 735, 700, 931, 912], [908, 901, 805, 815, 800, 831, 835], [705, 701, 702, 705, 710, 710, 711], [707, 731, 859, 913, 934, 931, 905]],	1))