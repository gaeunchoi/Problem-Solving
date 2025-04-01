function solution(today, terms, privacies) {
  let result = [];
  expiration = {};

  const [tY, tM, tD] = today.split(".");
  terms.forEach(term => {
    const [type, t] = term.split(" ");
    expiration[type] = t * 28;
  })

  privacies.forEach((privacy, idx) => {
    const [dates, type] = privacy.split(" ");
    const [pY, pM, pD] = dates.split(".");
    
    const [y, m, d] = [tY - pY, tM - pM, tD - pD];
    const total = 336*y + 28*m + d;
    if(expiration[type] <= total) result.push(idx+1);
  })

  return result;
}