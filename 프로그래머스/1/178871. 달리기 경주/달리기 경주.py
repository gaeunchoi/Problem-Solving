def solution(players, callings):
    answer = []
    ranks = {name: rank for rank, name in enumerate(players)}
    for call in callings:
        idx = ranks[call]

        ranks[call] -= 1
        ranks[players[idx-1]] += 1

        players[idx-1], players[idx] = players[idx], players[idx-1]

    return players