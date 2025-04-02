function solution(a, b, n) {
    var answer = 0;
    while(n >= a){
        const [ret, res] = [Math.floor(n/a), n%a];
        answer += ret * b;
        n = ret*b + res;
    }
    return answer;
}