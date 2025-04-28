function solution(survey, choices) {
    const totalType = ["RT", "CF", "JM", "AN"];
    const typeScore = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0};

    for (let i = 0; i < survey.length; i++) {
        const surveyType = survey[i];
        const disagree = surveyType[0];
        const agree = surveyType[1];
        const choice = choices[i];
        
        if (choice < 4) {
            typeScore[disagree] += 4 - choice;
        } else if (choice > 4) {
            typeScore[agree] += choice - 4;
        }
    }

    let result = "";
    for (let t of totalType) {
        const t1 = t[0];
        const t2 = t[1];
        result += typeScore[t1] >= typeScore[t2] ? t1 : t2;
    }

    return result;
}
