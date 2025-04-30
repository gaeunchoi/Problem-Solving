function solution(n) {
    let a = 0, b = 1;
    for (let i = 2; i <= n; i++) {
        [a, b] = [b, (a + b) % 1234567];
    }
    return b;
}