function convertTime(t){
  const [h, m] = [Math.floor(t/100), t%100];
  return 60*h + m;
}

function solution(schedules, timelogs, startday) {
  var answer = 0;
  for(let i = 0 ; i < schedules.length ; i++){
    let latework = false;
    let day = startday-1;
    let targetTime = convertTime(schedules[i]);
    for(let j = 0 ; j < timelogs[i].length ; j++){
      if([5, 6].includes(day)){
        day = (day+1) % 7;
        continue;
      } 
      
      let t = convertTime(timelogs[i][j]);

      if(t > targetTime + 10) {
        latework = true;
        break;
      } else day++;
    } 
    if(latework === false) answer++;
  }

  return answer;
}