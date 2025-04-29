import re

def solution(new_id):
    step_one_two = ''.join(re.findall(r'[a-z0-9\-_.]', new_id.lower()))
    step_three = re.sub(r'\.+', '.', step_one_two)
    step_four = step_three.strip('.')
    step_five = 'a' if len(step_four) == 0 else step_four
    step_six = step_five[:15].rstrip('.') if len(step_five) >= 16 else step_five
    if len(step_six) <= 2:
        step_six += step_six[-1] * (3 - len(step_six))
    
    return step_six
