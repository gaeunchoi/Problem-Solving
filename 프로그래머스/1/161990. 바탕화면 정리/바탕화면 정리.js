function solution(wallpaper) {
    let lux = -1, luy = -1, rdx = -1, rdy = -1;
    for(let i = 0 ; i < wallpaper.length ; i++){
        for(let j = 0 ; j < wallpaper[0].length ; j++){
            if(wallpaper[i][j] === "#"){
                if(lux === -1) lux = i;       // lux 찾기
                
                if(luy === -1) luy = j;
                else luy = Math.min(luy, j);  // luy 찾기
                
                rdx = i;                      // rdx 찾기 
                
                if(rdy === -1) rdy = j;
                else rdy = Math.max(rdy, j);
            } 
            
        }
    }
    return [lux, luy, rdx+1, rdy+1];
}

// 좋아요 많은 풀이 이거 짱이다 ,,
// function solution(wallpaper) {
//    let left = [];
//    let top = [];
//    let right = []
//    let bottom = [];
//    wallpaper.forEach((v,i) => {
//        [...v].forEach((val,ind) => {
//            if(val === "#") {
//                left.push(i)
//                top.push(ind)
//                right.push(i + 1)
//                bottom.push(ind + 1)
//            }
//        })
//    })
//    return [Math.min(...left), Math.min(...top), Math.max(...right), Math.max(...bottom)]
//}