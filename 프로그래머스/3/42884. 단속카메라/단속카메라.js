function solution(routes) {
    let sortedRoutes = routes.sort((a, b) => a[1] - b[1]);
    
    let result = 0;
    let camera = -30001;
    
    sortedRoutes.forEach(([s, e]) => {
        if(s > camera){
            camera = e;
            result++;
        }
    })
    return result;
}