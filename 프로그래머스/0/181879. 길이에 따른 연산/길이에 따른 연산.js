
const solution = num_list => num_list.length >= 11 ? num_list.reduce((a, b) => a+b, 0) : num_list.reduce((a, b) => a*b, 1);