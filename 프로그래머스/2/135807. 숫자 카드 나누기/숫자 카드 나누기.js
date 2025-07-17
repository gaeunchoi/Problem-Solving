const GCD = (a, b) => a % b ? GCD(b, a%b) : b
function solution(arrayA, arrayB) {
    let result = 0
    let [gcdA, gcdB] = [arrayA[0], arrayB[0]]
    for(let i = 1 ; i < arrayA.length ; i++){
        gcdA = GCD(gcdA, arrayA[i])
        gcdB = GCD(gcdB, arrayB[i])
    }
    
    if(gcdA === 1) gcdA = 0
    if(gcdB === 1) gcdB = 0
    
    if(arrayA.every((num) => num % gcdB !== 0)) result = Math.max(result, gcdB)
    if(arrayB.every((num) => num % gcdA !== 0)) result = Math.max(result, gcdA)
    
    return result
}