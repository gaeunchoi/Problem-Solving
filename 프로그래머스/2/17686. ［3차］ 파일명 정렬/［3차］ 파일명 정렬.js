function solution(files) {
    return files.sort((a, b) => {
        const regex = /([^\d]+)(\d{1,5})/;
        
        const [, headA, numA] = a.match(regex);
        const [, headB, numB] = b.match(regex);
        
        const [lowerHeadA, lowerHeadB] = [headA.toLowerCase(), headB.toLowerCase()];
        
        if(lowerHeadA < lowerHeadB) return -1;
        if(lowerHeadA > lowerHeadB) return 1;
        
        return +numA - +numB;
    });
}