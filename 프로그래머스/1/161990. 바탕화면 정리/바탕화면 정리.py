def solution(wallpaper):
    left = []
    top = []
    right = []
    bottom = []
    for i, v in enumerate(wallpaper):
        for idx, val in enumerate(v):
            if val == "#":
                left.append(i)
                top.append(idx)
                right.append(i+1)
                bottom.append(idx+1)
    return [min(left), min(top), max(right), max(bottom)]