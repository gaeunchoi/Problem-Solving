def solution(s):
    result = ''
    tmp = ''
    convertNum = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(len(s)):
        char = s[i]
        if(char.isdigit()):
            result += char
        else:
            tmp += char
            if tmp in convertNum:
                result += str(convertNum.index(tmp))
                tmp = ''
    
    return int(result)
            
    
    
