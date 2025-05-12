function solution(dirs) {
    let cx = 0, cy = 0;
    const visited = new Set();
    
    const directions = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1]};

    for (let dir of dirs) {
        const [dx, dy] = directions[dir];
        const mx = cx + dx;
        const my = cy + dy;

        if (mx >= -5 && mx <= 5 && my >= -5 && my <= 5) {
            const path = [[cx, cy], [mx, my]].sort().toString();
            visited.add(path);
            [cx, cy] = [mx, my];
        }
    }

    return visited.size;
}