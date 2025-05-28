function solution(numbers) {
    let answer = [];
    for(const num of numbers){
        if(num % 2 === 0) answer.push(num + 1);
        else {
            let binNum = "0" + num.toString(2);
            const idx = binNum.lastIndexOf("01");
            answer.push(parseInt(binNum.slice(0, idx) + "10" + binNum.slice(idx + 2), 2));
        }
    }
    return answer;
}