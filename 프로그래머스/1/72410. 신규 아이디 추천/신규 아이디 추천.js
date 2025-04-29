function solution(new_id) {
    const stepOneTwo = new_id.toLowerCase().match(/[a-z0-9-_.]/g).join("");
    const stepThree = stepOneTwo.replace(/\.+/g, ".");
    const stepFour = stepThree.replace(/^\.|\.$/g, "");
    const stepFive = stepFour.length === 0 ? "a" : stepFour;
    const stepSix = stepFive.length >= 16 ? stepFive.slice(0, 15).replace(/\.$/g, "") : stepFive;
    if(stepSix.length <= 2){
        const len = stepSix.length;
        const addChar = stepSix[len-1].repeat(3-len);
        const stepSeven = stepSix + addChar;
        return stepSeven;
    }
    return stepSix;
}