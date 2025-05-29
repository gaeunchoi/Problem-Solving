function solution(arr) {
    function compress(x, y, size) {
        const first = arr[x][y];
        let allSame = true;

        for (let i = x ; i < x + size ; i++) {
            for (let j = y ; j < y + size ; j++) {
                if (arr[i][j] !== first) {
                    allSame = false;
                    break;
                }
            }
            if (!allSame) break;
        }

        if (allSame) return first === 0 ? [1, 0] : [0, 1];

        const half = size / 2;
        const res1 = compress(x, y, half);
        const res2 = compress(x, y + half, half);
        const res3 = compress(x + half, y, half);
        const res4 = compress(x + half, y + half, half);
        return res1.map((val, idx) => val + res2[idx] + res3[idx] + res4[idx]);
  }

  return compress(0, 0, arr.length);
}
