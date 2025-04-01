const solution = (arr) => arr.reduce((acc, cur) => [...acc, ...new Array(cur).fill(cur)], []);
