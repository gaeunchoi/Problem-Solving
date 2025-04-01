// delete_list에 없으면 필터링
const solution = (arr, delete_list) => arr.filter((elem) => !delete_list.includes(elem))