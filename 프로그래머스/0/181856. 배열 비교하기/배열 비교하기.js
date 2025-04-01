function solution(arr1, arr2) {
    let length1 = arr1.length, length2 = arr2.length;
    if(length1 !== length2) return length1 < length2 ? -1 : 1
    
    let sum1 = arr1.reduce((acc, cur) => acc+cur, 0);
    let sum2 = arr2.reduce((acc, cur) => acc+cur, 0);
    if(sum1 !== sum2) return sum1 < sum2 ? -1 : 1
    else return 0
}