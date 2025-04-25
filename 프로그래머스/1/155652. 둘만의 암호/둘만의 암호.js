function solution(s, skip, index) {
    const alpha = "abcdefghijklmnopqrstuvwxyz";
    let noSkipAlpha = [...alpha].filter((v) => !skip.includes(v));
    return [...s].map((v) => noSkipAlpha[(noSkipAlpha.indexOf(v) + index) % noSkipAlpha.length]).join("");
}