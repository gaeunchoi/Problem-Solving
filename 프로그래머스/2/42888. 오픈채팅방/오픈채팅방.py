def solution(records):
    result = []
    id_name_match = {}
    for record in records:
        split_record = record.split()
        action = split_record[0]
        user_id = split_record[1]
        
        if action in ("Enter", "Change"):
            user_name = split_record[2]
            id_name_match[user_id] = user_name
            
        if action == "Enter":
            result.append([user_id, "IN"])
        elif action == "Leave":
            result.append([user_id, "OUT"])
            
    answer = []
    for uid, status in result:
        name = id_name_match[uid]
        if status == "IN":
            answer.append(f"{name}님이 들어왔습니다.")
        else:
            answer.append(f"{name}님이 나갔습니다.")
    return answer