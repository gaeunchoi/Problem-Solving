from collections import deque

def solution(dirs):
    cx, cy = 0, 0
    visited = set()
    directions = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1]}

    for dir in dirs:
        dx, dy = directions[dir]
        mx, my = cx + dx, cy + dy
        
        if -5 <= mx <= 5 and -5 <= my <= 5:
            visited.add(((cx, cy), (mx, my)) if (cx, cy) < (mx, my) else ((mx, my), (cx, cy)))
            cx, cy = mx, my
    return len(visited)