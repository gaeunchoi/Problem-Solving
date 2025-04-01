def solution(num_list):
  l, r = num_list[-2], num_list[-1]
  num_list.append(r-l if r>l else 2*r)
  return num_list