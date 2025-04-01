# 시간 초로 변환
def changeTime(time):
  m, s = map(int, time.split(":"))
  return 60*m + s

# 오프닝 구간 체크는 이동하기 전과 이동하고 나서 두 번 해야함
def checkOpening(s, e, c):
  if s <= c <= e:
    return e
  return c

def solution(video_len, pos, op_start, op_end, commands):
  # 전부 초로 변환
  video_len = changeTime(video_len)
  pos = changeTime(pos)
  op_start = changeTime(op_start)
  op_end = changeTime(op_end)

  for cmd in commands:
    pos = checkOpening(op_start, op_end, pos)

    # 앞으로 가기
    if cmd == "prev":
      pos -= 10
      if pos < 10:
        pos = 0
    # 뒤로 가기
    if cmd == "next":
      pos += 10
      if video_len - pos < 10:
        pos = video_len

    pos = checkOpening(op_start, op_end, pos)
  
  result_m, result_s = divmod(pos, 60)
  return f"{result_m:02d}:{result_s:02d}"