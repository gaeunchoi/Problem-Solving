function solution(myString, pat) {
    answer = myString.toUpperCase().includes(pat.toUpperCase()) ? 1 : 0;
    return answer;
}