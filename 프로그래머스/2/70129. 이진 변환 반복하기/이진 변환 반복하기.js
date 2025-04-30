function solution(s) {
    let result = 0;
    i = 0
    while(s !== "1"){
        const removeZero = s.replaceAll("0", "");
        result += s.length - removeZero.length;
        s = removeZero.length.toString(2);
        i++;
    }
    return [i, result];
}