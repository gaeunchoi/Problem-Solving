function getPermutations(arr, selectNum) {
    const result = [];
    if (selectNum === 1) return arr.map((v) => [v]);

    arr.forEach((fixed, idx, origin) => {
        const rest = origin.slice(0, idx).concat(origin.slice(idx + 1));
        const perms = getPermutations(rest, selectNum - 1);
        const attached = perms.map((perm) => [fixed, ...perm]);
        result.push(...attached);
    });

    return result;
}

function solution(k, dungeons) {
    const permutations = getPermutations(dungeons, dungeons.length);
    let maxCount = 0;

    for (const perm of permutations) {
        let curTired = k;
        let count = 0;

        for (const [minNeed, cost] of perm) {
            if (curTired >= minNeed) {
                curTired -= cost;
                count += 1;
            } else {
                break;
            }
        }

        maxCount = Math.max(maxCount, count);
    }

    return maxCount;
}