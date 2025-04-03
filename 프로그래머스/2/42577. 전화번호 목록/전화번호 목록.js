function solution(phone_book) {
    let phoneMap = new Map();
    
    for (let phone of phone_book) {
        phoneMap.set(phone, true);
    }

    // 각 번호를 한 글자씩 줄여가면서 접두어 검사
    for (let phone of phone_book) {
        let prefix = "";
        
        for (let num of phone) {
            prefix += num;
            if (prefix !== phone && phoneMap.has(prefix)) {
                return false;
            }
        }
    }
    return true; 
}