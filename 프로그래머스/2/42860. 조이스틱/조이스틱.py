# 상-하 이동: 알파벳 변경 횟수 === 아스키코드 값의 차이 이용
# 상-하 이동: B로 이동할 때, A -> B방향 또는 A -> Z방향 중 최소이동값
# 좌-우 이동: 
def solution(name):
    char_move = 0
    cursor_move = len(name) - 1
    ordA, ordZ = ord('A'), ord('Z')

    for idx, char in enumerate(name):
        # 상/하 이동 체크 -> 아스키코드값 체크
        ordChar = ord(char)
        char_move += min(ordChar - ordA, ordZ - ordChar + 1)

        # 해당 알파벳 다음부터 연속된 'A' 문자열 찾기
        next = idx + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        # 기존, 연속된 A 좌측 시작, 연속된 A 우측 시작 비교 갱신
        cursor_move = min(cursor_move, 2 * idx + len(name) - next, idx + 2 * (len(name) - next))
        
    return char_move + cursor_move