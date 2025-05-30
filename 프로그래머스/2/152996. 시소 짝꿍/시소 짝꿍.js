function solution(weights) {
  let result = 0;
  const ratios = [1 / 2, 2 / 3, 3 / 4];

  const countMap = new Map();
  for (const w of weights) {
    countMap.set(w, (countMap.get(w) || 0) + 1);
  }

  const uniqueWeights = [...new Set(weights)];

  for (const [w, count] of countMap.entries()) {
    if (count > 1) {
      result += (count * (count - 1)) / 2;
    }
  }

  for (const w of uniqueWeights) {
    for (const r of ratios) {
      const target = w * r;
      if (countMap.has(target)) {
        result += countMap.get(target) * countMap.get(w);
      }
    }
  }

  return result;
}