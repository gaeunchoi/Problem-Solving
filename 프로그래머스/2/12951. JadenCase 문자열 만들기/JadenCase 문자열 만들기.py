def solution(s):
    split_word = s.split(" ")
    result = []
    for sw in split_word:
        if sw:
            result.append(sw[0].upper() + sw[1:].lower())
        else:
            result.append("")
    return " ".join(result)