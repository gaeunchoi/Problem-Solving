function solution(nums) {
    const uniqueNums = new Set(nums);
    return Math.min(uniqueNums.size, Math.floor(nums.length / 2));
}