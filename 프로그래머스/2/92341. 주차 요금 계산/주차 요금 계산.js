function solution(fees, records) {
    const [basicTime, basicRate, unitTime, unitRate] = fees;
    
    let parking = new Map();
    let totalTime = new Map();
    
    for(const record of records){
        const [timeStr, car, type] = record.split(" ");
        const [h, m] = timeStr.split(":").map(Number);
        const time = 60*h + m;
        
        if(type === "IN"){
            parking.set(car, time);
        } else {
            const inTime = parking.get(car);
            const duration = time - inTime;
            totalTime.set(car, (totalTime.get(car) || 0) + duration);
            parking.delete(car);
        }
    }
    
    for(const [car, inTime] of parking.entries()){
        const duration = 1439 - inTime;
        totalTime.set(car, (totalTime.get(car) || 0) + duration);
    }
    
    const result = Array.from(totalTime.entries())
    .sort((a, b) => a[0].localeCompare(b[0]))
    .map(([car, time]) => {
        if(time <= basicTime) return basicRate;
        return basicRate + Math.ceil((time - basicTime) / unitTime) * unitRate;
    });
    
    return result;
}