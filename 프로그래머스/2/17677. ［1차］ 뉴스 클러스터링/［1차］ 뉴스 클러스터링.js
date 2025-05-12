function makeMultiset(str) {
  const multiset = new Map();
  str = str.toUpperCase();

  for (let i = 0; i < str.length - 1; i++) {
    const pair = str[i] + str[i + 1];
    if (/^[A-Z]{2}$/.test(pair)) {
      multiset.set(pair, (multiset.get(pair) || 0) + 1);
    }
  }
  return multiset;
}

function solution(str1, str2) {
  const multiset1 = makeMultiset(str1);
  const multiset2 = makeMultiset(str2);

  let intersectionSize = 0;
  let unionSize = 0;
  const allKeys = new Set([...multiset1.keys(), ...multiset2.keys()]);

  for (const key of allKeys) {
    const count1 = multiset1.get(key) || 0;
    const count2 = multiset2.get(key) || 0;
    intersectionSize += Math.min(count1, count2);
    unionSize += Math.max(count1, count2);
  }

  if (unionSize === 0) {
    return 65536;
  }

  return Math.floor((intersectionSize / unionSize) * 65536);
}