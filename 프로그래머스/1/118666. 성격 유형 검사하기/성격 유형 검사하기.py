def solution(survey, choices):
    total_type = ["RT", "CF", "JM", "AN"]
    type_score = {"R": 0, "T" : 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    
    for idx, survey_type in enumerate(survey):
        disagree, agree = survey_type[0], survey_type[1]
        choice = choices[idx]
        if choice < 4:
            type_score[disagree] += 4-choice
        elif choice > 4:
            type_score[agree] += choice - 4
            

    result = ""
    for t in total_type:
        t1, t2 = t[0], t[1]
        result += t1 if type_score[t1] >= type_score[t2] else t2
    return result