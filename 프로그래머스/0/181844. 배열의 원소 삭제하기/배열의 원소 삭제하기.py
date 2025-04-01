def solution(arr, delete_list):
  for elem in delete_list:
    if elem in arr:
      arr.remove(elem)
  return arr