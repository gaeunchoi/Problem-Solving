const convertTime = (t) => {
    const [h, m] = t.split(":").map(Number);
    return 60*h + m;
}

function solution(book_time) {
    const sortedBookTime = book_time.map(([s, e]) => [convertTime(s), convertTime(e) + 10]).sort((a, b) => a[0] - b[0]);
    
    let rooms = [];
    for(const [s, e] of sortedBookTime){
        let used = false;
        for(let i = 0 ; i < rooms.length; i++){
            if(rooms[i] <= s){
                rooms[i] = e;
                used = true;
                break;
            }
        }
        
        if(!used) rooms.push(e);
    }
    
    return rooms.length;
}