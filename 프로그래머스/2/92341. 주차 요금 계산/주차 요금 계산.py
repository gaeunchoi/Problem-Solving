import math
from collections import defaultdict

def solution(fees, records):
    basic_time, basic_rate, unit_time, unit_rate = fees
    parking = {}
    total_time = defaultdict(int)

    for record in records:
        time_str, car, status = record.split()
        h, m = map(int, time_str.split(":"))
        minutes = h * 60 + m

        if status == "IN":
            parking[car] = minutes
        else:
            total_time[car] += minutes - parking.pop(car)

    for car, in_time in parking.items():
        total_time[car] += 1439 - in_time 

    result = []
    for car in sorted(total_time):
        time = total_time[car]
        if time <= basic_time:
            result.append(basic_rate)
        else:
            extra = math.ceil((time - basic_time) / unit_time)
            result.append(basic_rate + extra * unit_rate)

    return result
