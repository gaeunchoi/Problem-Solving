def solution(bandage, health, attacks):

    bandtime, healpertime, fullheal = bandage[0], bandage[1], bandage[2]
    user_time, user_health = 0, health
    for attack_time, attack_demage in attacks:
        # 공격받기 전까지 체력변화량 확인
        save_time= (attack_time-1) - user_time
        user_health += (save_time//bandtime) * fullheal + save_time * healpertime
        user_time = attack_time
        if user_health >= health:
            user_health = health

        # 공격받은 후 체력변화량 확인
        user_health -= attack_demage
        if user_health <= 0:
             return -1

    return user_health