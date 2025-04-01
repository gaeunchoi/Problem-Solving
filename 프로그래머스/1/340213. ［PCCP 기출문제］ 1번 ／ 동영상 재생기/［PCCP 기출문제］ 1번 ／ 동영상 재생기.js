// 모든 분-초로 되어있는 시간을 초로 바꾸기
// prev -> 10초를 빼주고, pos가 10 이하일 경우 0으로 바꾸기
// next -> 10초를 더해주고, 전체 길이 - pos가 10 이하일 경우 전체길이로 바꾸기
// 오프닝 체크는 명령을 수행하기 전/후로 둘다 체크하기
const changeTime = (time) => {
  const [m, s] = time.split(":")
  return +m*60 + +s
}

// 오프닝 시작, 오프닝 끝, 현재 위치 비교
const checkOpening = (s, e, c) => {
  if(s <= c && c <= e) return e
  return c
}

function solution(video_len, pos, op_start, op_end, commands) {
  video_len = changeTime(video_len)
  pos = changeTime(pos)
  op_start = changeTime(op_start)
  op_end = changeTime(op_end)
  
  commands.forEach((cmd) => {
    pos = checkOpening(op_start, op_end, pos);

    if(cmd === "prev"){
      pos -= 10
      if(pos < 10) pos = 0
    } else {
      pos += 10
      if(video_len - pos < 10) pos = video_len
    }

    pos = checkOpening(op_start, op_end, pos);
  })

  const [result_m, result_s] = [Math.floor(pos / 60).toString().padStart(2, "0"), (pos%60).toString().padStart(2, "0")]
  return result_m + ":" + result_s
}