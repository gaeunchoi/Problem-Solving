def solution(s):
    split_word = s.split(" ")
    result = []
    for sw in split_word:
        if sw:  # 비어있지 않은 단어면 처리
            result.append(sw[0].upper() + sw[1:].lower())
        else:  # 빈 문자열 (공백)인 경우 그대로 유지
            result.append("")
    return " ".join(result)