const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

rl.on("line", (line) => {
  input.push(line.trim());
}).on("close", () => {
  const [N, M] = input[0].split(" ").map(Number);

  let gItem = new Set(input[1].split(" "));
  let fItem = new Set(input[2].split(" "));

  for (let i = 0; i < M; i++) {
    const [a, b] = input[3 + i].split(" ");

    if (gItem.has(a) && fItem.has(b)) {
      gItem.delete(a);
      fItem.delete(b);
			
      gItem.add(b);
      fItem.add(a);
    }
  }

  const sortedItems = Array.from(gItem).sort();
  console.log(sortedItems.join(" "));
});
