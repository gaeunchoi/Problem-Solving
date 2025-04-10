function solution(babbling) {
  const talk = ["aya", "ye", "woo", "ma"];
  let count = 0;

  babbling.forEach(word => {
    let current = word;
    let prev = "";

    while (current.length > 0) {
      const match = talk.find(t => current.startsWith(t) && t !== prev);
      if (!match) return; 

      prev = match;
      current = current.slice(match.length);
    }
    count++;
  });

  return count;
}
