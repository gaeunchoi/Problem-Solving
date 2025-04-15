const convertTime = (time) => {
    const [h, m] = time.split(":").map(Number);
    return h * 60 + m;
};

function solution(plans) {
    // 시작 시간 기준으로 정렬
    plans.sort((a, b) => convertTime(a[1]) - convertTime(b[1]));

    const result = [];
    const stack = [];

    for (let i = 0; i < plans.length; i++) {
        let [name, startTime, duration] = plans[i];
        let currentTime = convertTime(startTime);
        duration = Number(duration);

        const nextStartTime = i + 1 < plans.length ? convertTime(plans[i + 1][1]) : Infinity;

        let endTime = currentTime + duration;

        if (endTime <= nextStartTime) {
            result.push(name);
            currentTime = endTime;

            while (stack.length > 0) {
                const [pausedName, remainingTime] = stack.pop();
                if (currentTime + remainingTime <= nextStartTime) {
                    currentTime += remainingTime;
                    result.push(pausedName);
                } else {
                    const used = nextStartTime - currentTime;
                    stack.push([pausedName, remainingTime - used]);
                    break;
                }
            }
        } else {
            const remaining = duration - (nextStartTime - currentTime);
            stack.push([name, remaining]);
        }
    }

    while (stack.length > 0) {
        const [name] = stack.pop();
        result.push(name);
    }

    return result;
}
